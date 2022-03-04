cd ..
cd src/database/

read -p "Enter your MySQL username: " username
read -p "Enter password: " password

echo "Getting to work..."

mysql -u $username -p $password EventManagementSystem < database.sql
mv config.json.example config.json
sed -e "s/\${username}/$username/" -e "s/\${password}/$password/" config.json | tee config.json

echo "Setup complete!"
