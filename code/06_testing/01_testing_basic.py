# TDD is the back bone for sucessfull CI/CD pipeline.
# CI/CD to complex, helps in saving a lot of cost in long run.
# There are 3 types of test.
# 1. Unit test : test the smallest degree of functionality, like a function.
# 2. Integration test : test how different modules integrate with each other.
# 3. Functional test : full functionality of the application is tested.

# assert is good way of checking sanity of a program.
# It should never be used in production as these can be disabled by using a flag.
# True :  means the execution will continue.
# False : means the execution will stop
a = 5
assert a > 1
assert a < 1

print("Hello")