import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('hello_api.yaml')

if __name__ == '__main__':
    app.run(port=5000)