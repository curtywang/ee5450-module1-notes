import pytest
import some_module as sm


def test_add5():
    assert sm.add5(2) == 7
    assert sm.add5(-1000000) == -999995
    assert sm.add5(0) == 5


def test_quadratic_formula():
    with pytest.raises(ValueError):
        sm.quadratic_formula(0.0, 0.0, 0.0)
        sm.quadratic_formula(1., 1., 1.)
    assert sm.quadratic_formula(1., 0., 0.) == (0.0, 0.0)
    assert sm.quadratic_formula(1., 1., 0.) == (0.0, -1.0)


if __name__ == '__main__':
    pytest.main()
