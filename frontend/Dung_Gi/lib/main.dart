import 'package:flutter/material.dart';
import 'properties_tab.dart';
import 'agents_tab.dart';
import 'bulletin_board_tab.dart';


void main() {
  runApp(RealEstateApp());
}

class RealEstateApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dung-Gi',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  Widget _buildBody() {
    switch (_selectedIndex) {
      case 0:
        return PropertiesTab();
      case 1:
        return AgentsTab();
      case 2:
        return BulletinBoardTab();
      default:
        return Text('Unknown tab');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Dung-Gi'),
      ),
      body: _buildBody(),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Properties',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.people),
            label: 'Agents',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.message),
            label: 'Bulletin Board',
          ),
        ],
        currentIndex: _selectedIndex,
        onTap: (index) {
          setState(() {
            _selectedIndex = index;
          });
        },
      ),
    );
  }
}
