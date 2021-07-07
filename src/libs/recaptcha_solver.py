from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from python_anticaptcha import AnticatpchaException, ImageToTextTask

def solver():
    api_key = ''
    site_key = '6Lc_91wUAAAAAAJQSXHEk4yfZah0a1VMLNBZ_CIE'
    url = 'https://chat-avenue.com'

    try:
        client = AnticaptchaClient(api_key)
        task = NoCaptchaTaskProxylessTask(url, site_key)
        job = client.createTask(task)
        job.join()
        return job.get_solution_response()

    except AnticatpchaException as e:
        if e.error_code == 'ERROR_ZERO_BALANCE':
            print(e.error_code)
        else:
            raise