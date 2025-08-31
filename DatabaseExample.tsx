
import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { openDatabase } from 'react-native-sqlite-storage';

const db = openDatabase({ name: 'test.db' });

const DatabaseExample = () => {
  const [data, setData] = useState('');

  useEffect(() => {
    db.transaction(txn => {
      txn.executeSql(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'",
        [],
        (tx, res) => {
          if (res.rows.length === 0) {
            txn.executeSql('DROP TABLE IF EXISTS users', []);
            txn.executeSql(
              'CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name VARCHAR(20), user_contact INT(10), user_address VARCHAR(255))',
              []
            );
          }
        }
      );
    });

    db.transaction(txn => {
      txn.executeSql(
        "INSERT INTO users (user_name, user_contact, user_address) VALUES (?,?,?)",
        ['John Doe', 1234567890, '123 Main St'],
        (tx, results) => {
          console.log('Results', results.rowsAffected);
          if (results.rowsAffected > 0) {
            console.log('Data Inserted Successfully');
          } else {
            console.log('Insert failed');
          }
        }
      );
    });

    db.transaction(txn => {
      txn.executeSql(
        "SELECT * FROM users",
        [],
        (tx, results) => {
          var temp = [];
          for (let i = 0; i < results.rows.length; ++i) {
            temp.push(results.rows.item(i));
          }
          setData(JSON.stringify(temp));
        }
      );
    });
  }, []);

  return (
    <View style={styles.container}>
      <Text>Database Example</Text>
      <Text>{data}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default DatabaseExample;
