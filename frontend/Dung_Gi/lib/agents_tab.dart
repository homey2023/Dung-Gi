import 'package:flutter/material.dart';
import 'agent_details_dialog.dart';


class AgentsTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
      ),
      itemCount: 10,
      itemBuilder: (context, index) {
        return GestureDetector(
          onTap: () {
            showDialog(
              context: context,
              builder: (BuildContext context) {
                return AgentDetailsDialog(index: index);
              },
            );
          },
          child: Card(
            child: Stack(
              children: [
                Column(
                  children: [
                    Text('Agent $index'),
                    Text('Agent details'),
                  ],
                ),
                Positioned(
                  top: 4,
                  right: 4,
                  child: Icon(
                    Icons.star,
                    color: Colors.grey,
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
