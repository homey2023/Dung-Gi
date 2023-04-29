import 'package:flutter/material.dart';
import 'property_details_dialog.dart';

class PropertiesTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: 10,
      itemBuilder: (context, index) {
        return ListTile(
          leading: Image.network(
            'https://via.placeholder.com/50', // Replace with your own image URL or local asset
            width: 50,
            height: 50,
            fit: BoxFit.cover,
          ),
          title: Text('Property $index'),
          subtitle: Text('Property details'),
          onTap: () {
            showDialog(
              context: context,
              builder: (BuildContext context) {
                return PropertyDetailsDialog(index: index);
              },
            );
          },
        );
      },
    );
  }
}
