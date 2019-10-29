import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

SUCCESS_CODE = 0
FAIURE_CODE = 1
CUST_ADDONS_DIR = "/home/mattobell/Desktop"
CUST_ADDONS_NAME = 'custom_addons'
BRANCH_TO_DEPLOY = 'master'


@app.route("/")
def index():
    return "Good request"


@app.route("/test_result", methods=['POST'])
def get_result():
    data = request.form
    data = dict(data)
    data_val = data.get('payload')
    valid_data = json.loads(data_val)
    success_or_failure = valid_data.get('status')
    branch = valid_data.get('branch')
    if success_or_failure == SUCCESS_CODE and branch == BRANCH_TO_DEPLOY:
        current_directory = os.getcwd()
        if current_directory == CUST_ADDONS_DIR:
            directory_contents = os.listdir(os.getcwd())
            if CUST_ADDONS_NAME not in directory_contents:
                os.system(
                    "git clone -b {} --single-branch --depth=1 https://github.com/sob0808/kjm.git {}".format(BRANCH_TO_DEPLOY, CUST_ADDONS_NAME)
                )
            else:
                try:
                    os.chdir(CUST_ADDONS_NAME)
                    os.system("git pull origin master")
                except Exception:
                    print(f"Error occurred!")
        return json.dumps({"completed_successfully": True})
    return json.dumps({"completed_successfully": False})
