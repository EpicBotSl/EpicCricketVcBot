echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/EpicBotSl/EpicCricketVcBot.git /EpicCricketVcBot
cd /EpicCricketVcBot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 main.py
