# main.py
from flask import Flask
from flask_restful import Api
from blockchain import BlockchainResource, MineBlockResource, IsValidResource

app = Flask(__name__)
api = Api(app)

blockchain = Blockchain()

# Routes
api.add_resource(MineBlockResource, '/mine_block', resource_class_kwargs={'blockchain': blockchain})
api.add_resource(BlockchainResource, '/get_chain', resource_class_kwargs={'blockchain': blockchain})
api.add_resource(IsValidResource, '/is_valid', resource_class_kwargs={'blockchain': blockchain})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
