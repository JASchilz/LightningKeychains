import subprocess
import json

def get_invoice(request_hash):
    result = subprocess \
        .run(["lncli", "lookupinvoice", request_hash], stdout=subprocess.PIPE)

    if result.returncode == 0:
        return json.loads(result.stdout.decode())
    else:
        return None

def make_invoice(cost_satoshis):
    result = subprocess \
        .run(["lncli", "addinvoice", str(cost_satoshis)], stdout=subprocess.PIPE)

    if result.returncode == 0:
        return json.loads(result.stdout.decode())
    else:
        return None

