from flaskapp import app, db

# from FlaskApp.APIs.User_APIs import User_Apis
# from FlaskApp.APIs.gps_tracker_api import gps_tracker_api
# from FlaskApp.APIs.Device_APIs import Device_Apis
# from FlaskApp.APIs.static_files import static_files
# from FlaskApp.APIs.Raw_data_APIs import raw_data_api
# from FlaskApp.APIs.plug_APIs import plug_api


# db.create_all()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app.config["server_port"])