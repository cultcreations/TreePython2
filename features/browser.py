from selenium import webdriver


class Browser(object):
    #driver = webdriver.Chrome()
    driver = webdriver.Remote(command_executor= 'http://192.168.16.215:4444/wd/hub',
                              desired_capabilities= {
                                  'browserName': 'chrome',
                                  'javascriptEnabled': True
                              })
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()


def close(context):
        context.driver.close()

