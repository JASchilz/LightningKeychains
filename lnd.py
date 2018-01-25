import subprocess
import json

class LNDConnectionError(RuntimeError):
    pass

class LNCLIRuntimeError(RuntimeError):
    pass

def _lncli_execute(lncli_args):
    """
    Helper function that runs lncli with the given arguments, and returns the
    result as a dictionary. All elements of the list of arguments must be strings

    Eg: _lncli_execute(["addinvoice", "2000"])
    Returns: { "r_hash": "3ab56...", "pay_req": "lntb5738nmq70..."}

    See "lncli help" for details on what to expect from executing lncli.
    """

    command = ["lncli"] + lncli_args

    completed_process = subprocess.run(command, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        return json.loads(completed_process.stdout.decode())
    else:
        if "the connection is unavailable" in completed_process.stdout.decode():
            raise LNDConnectionError("Could not connect to LND process.")
        else:
            raise LNCLIRuntimeError

def make_invoice(cost_satoshis):
    return _lncli_execute(["addinvoice", str(cost_satoshis)])

def get_invoice(request_hash):
    return _lncli_execute(["lookupinvoice", request_hash])

def get_info():
    return _lncli_execute(["getinfo"])

