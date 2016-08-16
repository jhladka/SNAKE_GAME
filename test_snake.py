# -*- coding: utf-8 -*-
import pytest
import snake_game as s

def sample_snake():
    return [(2, 4), (3, 4), (3, 3), (3, 2), (4, 2)]


def sample_snake2():
    return [(2, 4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 1), (4, 0)]
    

def test_move_to_S():
    snake = sample_snake()
    s.move(snake, 'S') 
    assert snake == [(3, 4), (3, 3), (3, 2), (4, 2), (4, 3)]
    

def test_invalid_move_back():
    snake = sample_snake()
    with pytest.raises(ValueError) as excinfo:
        s.move(snake, 'W')
    assert excinfo.value.message == 'Game over!'


def test_invalid_move_out():
    snake = sample_snake2()
    with pytest.raises(ValueError) as excinfo:
        s.move(snake, 'N')
    assert excinfo.value.message == 'Game over!'
    