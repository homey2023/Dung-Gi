import 'package:flutter/material.dart';

class PostDetailsPage extends StatelessWidget {
  final int postIndex;

  PostDetailsPage({required this.postIndex});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Post Details'),
      ),
      body: Column(
        children: [
          ListTile(
            title: Text('Post $postIndex'),
            subtitle: Text('Post details'),
          ),
          Divider(),
          Expanded(
            child: ListView.builder(
              itemCount: 5,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text('Comment $index'),
                  subtitle: Text('Comment details'),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Write a comment...',
                border: OutlineInputBorder(),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
