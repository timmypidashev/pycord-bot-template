echo "--------------------------"
echo "Installing dependencies..."
echo "--------------------------"

sleep 1

pipreqs --force --ignore ./External/ .
pip install -r requirements.txt

cd ./External/pycord/ && python3 -m pip install -U . && cd ../..
cd ./External/asqlite/ && python3 -m pip install -U . && cd ../..

echo "-------------------------------------------------------------------------"
echo "Done! Configure your '.env' file and run 'client.py' to start up the bot!"
echo "-------------------------------------------------------------------------"