def calculate(a,b, operation):
    result = None
    
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    
    print({
        'statusCode': 200,
        'body': str(result)
    })

calculate(1,2,'add')

#Output Like {'statusCode': 200, 'body': '3'}