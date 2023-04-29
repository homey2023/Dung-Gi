import 'package:flutter/material.dart';

class PropertyDetailsDialog extends StatelessWidget {
  final int index;

  PropertyDetailsDialog({required this.index});

  @override
  Widget build(BuildContext context) {
    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12.0)),
      child: Padding(
        padding: const EdgeInsets.all(12.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('Property $index'),
            SizedBox(height: 8),
            Text('Detailed information about Property $index'),
            SizedBox(height: 24),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('Close'),
            ),
          ],
        ),
      ),
    );
  }
}
