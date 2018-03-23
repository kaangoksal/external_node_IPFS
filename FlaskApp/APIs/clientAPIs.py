from flask import request, make_response
import json
import re
import uuid
from flaskapp import db, app
from werkzeug import secure_filename

import subprocess
import os
import time
import select

class client_APIs:

    @staticmethod
    def upload_file_to_IPFS():
        if request.method == 'POST':
            f = request.files['file']

            # We are putting the file to a random folder which we will delete quite soon after uploading it to IPFS
            random_folder = str(uuid.uuid4())
            absolute_file_name ="./" + random_folder + secure_filename(f.filename)
            f.save(absolute_file_name)

            # "ipfs add myriad.pdf.gpg" command that lets us add shit

            command = "ipfs add " + absolute_file_name

            try:
                ipfs_upload_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                                    preexec_fn=os.setsid)

                turns = 0
                while 1:

                    # The select function checks whether any of these pipes are ready to read,
                    # as I remember this was a non blocking call.

                    readable, writable, e = select.select([ipfs_upload_process.stdout, ipfs_upload_process.stderr], [], [], 1)

                    # This can cause CPU sping, so we might add a slight delay?
                    if len(readable) > 0:

                        return_message = ""
                        for pipe in readable:
                            output = b''
                            byte_read = None
                            while byte_read != b'':
                                byte_read = pipe.read(1)
                                output += byte_read
                            return_message += output.decode("utf-8")

                        print("IPFS upload successfull")
                        dict_local = {"code": 200,
                                      "hash": return_message, "message": "IPFS upload successful"}
                        return json.dumps(dict_local)

                    elif turns > 10:

                        print("Result Expired, did not get any reply")
                        dict_local = {"code": 400,
                                      "message": "upload to IPFS Failed, file will be kept for debugging purposes"}
                        return json.dumps(dict_local)

                    else:

                        time.sleep(0.5)
                        turns += 1

            except Exception as e:

                dict_local = {"code": 400, "message": "upload to IPFS Failed, file will be kept for debugging purposes"}
                return json.dumps(dict_local)





app.add_url_rule('/api/upload_file_to_ipfs', 'upload_file_to_ipfs', client_APIs.upload_file_to_IPFS, methods=['POST'])






