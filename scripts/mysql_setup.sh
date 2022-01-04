cd ..
cd src/database/
mysql -u <USERNAME> -p <PASSWORD> EventManagementSystem < database.sql
mv config.json.example mv config.json
echo "Setup complete!"