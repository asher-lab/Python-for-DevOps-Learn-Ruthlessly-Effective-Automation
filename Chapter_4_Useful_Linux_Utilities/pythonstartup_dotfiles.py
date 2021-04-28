import types
import uuid

helpers = types.ModuleType('helpers')
helpers.uuid = uuid.uuid4()

#usage
#export PYTHONSTARTUP=pythonstartup.py python3
# >>helpers
# >>helpers.uuid4()
