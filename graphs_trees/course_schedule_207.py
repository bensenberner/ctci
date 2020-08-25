"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
from collections import defaultdict


def canFinish(numCourses, prerequisites):
    prereq_to_course = defaultdict(lambda: set())
    course_to_prereq = defaultdict(lambda: set())
    courses_in_chain = set()
    for course, prereq in prerequisites:
        prereq_to_course[prereq].add(course)
        course_to_prereq[course].add(prereq)
        courses_in_chain.add(prereq)
        courses_in_chain.add(course)
    courses_with_prereqs = course_to_prereq.keys()
    courses_without_prereqs = courses_in_chain - courses_with_prereqs
    while courses_without_prereqs and courses_in_chain:
        course = courses_without_prereqs.pop()
        courses_in_chain.remove(course)
        if course not in prereq_to_course:
            continue
        for downstream_course in prereq_to_course.get(course):
            course_to_prereq[downstream_course].remove(course)
            if not course_to_prereq[downstream_course]:
                courses_without_prereqs.add(downstream_course)
    return not bool(courses_in_chain)


print(canFinish(2, [[0, 1]]))
