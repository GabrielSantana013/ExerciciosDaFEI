import re

from hypothesis import given, strategies as st

from romanos import de_romano, para_romano


NUMERAL_CANONICO = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)


@given(st.integers(min_value=1, max_value=3999))
def test_ida_e_volta(n):
    assert de_romano(para_romano(n)) == n


@given(st.integers(min_value=1, max_value=3999))
def test_numeral_gerado_e_canonico(n):
    assert NUMERAL_CANONICO.fullmatch(para_romano(n))