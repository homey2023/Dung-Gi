import 'package:flutter/material.dart';

class AgentDetailsDialog extends StatelessWidget {
  final int index;

  AgentDetailsDialog({required this.index});

  @override
  Widget build(BuildContext context) {
    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12.0)),
      child: Padding(
        padding: const EdgeInsets.all(12.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('Agent $index'),
            SizedBox(height: 8),
            Text('Detailed information about Agent $index'),
            SizedBox(height: 24),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                ElevatedButton.icon(
                  onPressed: () {
                    // Implement call functionality
                  },
                  icon: Icon(Icons.call),
                  label: Text('Call'),
                ),
                ElevatedButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text('Close'),
                ),
                IconButton(
                  onPressed: () {
                    // Implement favorite (star) functionality
                  },
                  icon: Icon(Icons.star, color: Colors.yellow),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
