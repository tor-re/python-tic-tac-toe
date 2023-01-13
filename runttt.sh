#!
cd ./python-tic-tac-toe
if [ ! -x tictactoe.py ] 
then 
  chmod +x setupttt.sh 
  echo "uh oh... lets setup"
  ./settup.sh
  sleep 1 
  echo "all good"
fi
python3 ./tictactoe.py
