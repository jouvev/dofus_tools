@echo off
set PYTHONPATH=%PYTHONPATH%;.
cd ..
python src/main.py --nodebug
pause