import pytest
import helloWorld

def test_Hello():
    assert helloWorld.Hello()=="Hello World!"

def test_HelloUser():
    assert helloWorld.Hello('USER')=="Hello World USER!"