**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virt env

```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual edvironemnt.

```
python3 -m backend.data
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app
```