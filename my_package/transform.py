import apache_beam as beam

def filter_cart_requests(request):
    return 'cart.jsp' in request

def load_apache_logs(pipeline, input_path):    
    return pipeline | "LOAD" >> beam.io.ReadFromText(input_path)