// ========================================
// CREATE
// ========================================

// Create a Student
CREATE (s:Student {
    id: "S100",
    name: "Demo Student",
    city: "Delhi",
    demo: true
})
RETURN s;


// Create a Course using parameters
CREATE (c:Course {
    id: $course_id,
    title: $course_title,
    demo: true
})
RETURN c;


// Create a relationship
MATCH (s:Student {id: "S100"})
MATCH (c:Course {id: $course_id})
CREATE (s)-[:ENROLLED_IN]->(c)
RETURN s, c;


// ========================================
// READ
// ========================================

// Read all students
MATCH (s:Student)
RETURN s
ORDER BY s.name;


// Read students and enrolled courses
MATCH (s:Student)-[r:ENROLLED_IN]->(c:Course)
RETURN s, r, c;


// Read mentors and courses
MATCH (m:Mentor)-[r:TEACHES]->(c:Course)
RETURN m, r, c;


// Read courses and skills
MATCH (c:Course)-[r:TEACHES_SKILL]->(skill:Skill)
RETURN c, r, skill;


// Find students learning Python
MATCH (s:Student)
      -[:ENROLLED_IN]->
      (c:Course)
      -[:TEACHES_SKILL]->
      (skill:Skill)

WHERE skill.name = "Python"

RETURN s, c, skill;


// Find projects using Neo4j
MATCH (p:Project)-[:USES]->(skill:Skill)

WHERE skill.name = "Neo4j"

RETURN p, skill;


// ========================================
// UPDATE
// ========================================

// Update student city
MATCH (s:Student {
    id: $student_id
})

SET s.city = $city

RETURN s;


// Update course level
MATCH (c:Course {
    id: $course_id
})

SET c.level = $level

RETURN c;


// ========================================
// DELETE RELATIONSHIP
// ========================================

MATCH (
    s:Student {
        id: $student_id
    }
)-[r:INTERESTED_IN]->(
    c:Company {
        id: $company_id
    }
)

DELETE r;


// ========================================
// DELETE NODE
// ========================================

MATCH (p:Project {
    id: $project_id
})

DETACH DELETE p;


// ========================================
// GRAPH VISUALIZATION
// ========================================

MATCH (n)-[r]->(m)

WHERE n.demo = true
  AND m.demo = true

RETURN n, r, m;


// ========================================
// NODE COUNTS
// ========================================

MATCH (n)

WHERE n.demo = true

RETURN
    labels(n) AS label,
    count(n) AS total

ORDER BY label;


// ========================================
// RELATIONSHIP COUNTS
// ========================================

MATCH (a)-[r]->(b)

WHERE a.demo = true
  AND b.demo = true

RETURN
    type(r) AS relationship,
    count(r) AS total

ORDER BY relationship;