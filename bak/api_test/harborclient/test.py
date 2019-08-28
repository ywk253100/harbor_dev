import swagger_client

print "Hello"

cfg = swagger_client.Configuration()
cfg.host = "http://10.192.157.74/api"
cfg.username = "admin"
cfg.password = "Harbor123456"
cfg.verify_ssl = False
cfg.debug = True
api_client = swagger_client.ApiClient(cfg)
api_instance = swagger_client.ProductsApi(api_client)
result, other, b = api_instance.configurations_get_with_http_info()
print("==========================")
print(result)
print(other)
print(b)
swagger_client.ApiClient
swagger_client.ProductsApi