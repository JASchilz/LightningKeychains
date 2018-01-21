import subprocess
import json

def _process_result(completed_process):
    if completed_process.returncode == 0:
        return json.loads(completed_process.stdout.decode())
    else:
        return None

def get_invoice(request_hash):
    result = subprocess \
        .run(["lncli", "lookupinvoice", request_hash], stdout=subprocess.PIPE)

    return _process_result(result)


def make_invoice(cost_satoshis):
    result = subprocess \
        .run(["lncli", "addinvoice", str(cost_satoshis)], stdout=subprocess.PIPE)

    return _process_result(result)

def get_info():
    result = subprocess.run(["lncli", "getinfo"], stdout=subprocess.PIPE)

    return _process_result(result)

