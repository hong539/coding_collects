#Play with bing-gpt
#Cloud you write some Python codes to compare these three protocols: http/websocket/grpc ?
import requests
import websocket
import grpc

# HTTP request
response = requests.get('http://example.com')
print(response.status_code)

# WebSocket connection
ws = websocket.create_connection('ws://echo.websocket.org/')
ws.send('Hello, World!')
result = ws.recv()
print(result)

# gRPC connection
channel = grpc.insecure_channel('localhost:50051')
stub = helloworld_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
print(response.message)