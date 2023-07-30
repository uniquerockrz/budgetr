pip uninstall -y ledgerlib
rm -rf lib/dist
python -m build lib
python -m pip install lib/dist/*.whl