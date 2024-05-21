from website import create_app #create_app function  imported from website module
                               #this function configure flask app

app = create_app()# created flask app instance and assigned to app variable

if __name__ == '__main__':#if script is being executed directly or imported as module
    app.run(debug=True)  #this line starts flask development server
