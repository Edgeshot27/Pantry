echo "BUILD START"
python3.12 -m pip install -r requirementx.txt
python3.12 manage.py collectstatic --noinput --clear
ech "BUILD END"