# Learning Platform Graph Explanation

## 1. Nodes

A node represents an entity in our learning platform.

The project contains six node labels.

| Label   | Description                        |
| ------- | ---------------------------------- |
| Student | Person learning courses            |
| Course  | Learning course                    |
| Mentor  | Person teaching courses            |
| Skill   | Technical skill                    |
| Project | Project built by students          |
| Company | Company a student is interested in |

Example:

```cypher
(s:Student)
```
