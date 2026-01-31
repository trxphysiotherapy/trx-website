# build_files.sh
echo "Building the project..."
python3.12 -m pip install -r requirements.txt --break-system-packages
python3.12 manage.py collectstatic --noinput
echo "Build finished ✅."
