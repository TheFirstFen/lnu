# Directed Graph String

edges logic is (v1 --> v2) Due to it possibly being easier to sort oppisite way around first and then reversing it.

adding edges where v1 is the course in question and v2 is the prerequisuite.

want to sort the courses in oppisite order first by starting with the course with none pointing to it (meaning it is none of the edges v2).

which in out case would make this a type of tree where nodes could have seveeral parents and children. the depth of the node is determined by the parent with the deepest depth meaning the node in question should be the deepest parents depth + 1.

bfs(Root vertex) -> reverse??
