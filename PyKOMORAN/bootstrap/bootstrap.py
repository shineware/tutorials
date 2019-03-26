#!/usr/bin/env python
# coding: utf-8

#
# 3줄의 코드로 형태소 분석 시작하기
#
# PyKomoran을 이용하여 3줄의 코드로 형태소 분석을 따라해보도록 하겠습니다.
# 이 내용은 [PyKOMORAN 문서 사이트](https://docs.komoran.kr/pykomoran/tutorial.html)에서 확인하실 수 있습니다.

# PyKomoran 설치
#
# 자세한 설치 관련한 내용은 [PyKomoran 설치하기](https://docs.komoran.kr/pykomoran/installation.html) 문서를 참고해주시기 바랍니다.

# PyKomoran 불러오기
#
# 다음과 같이 PyKomoran을 불러옵니다.

from PyKomoran import *

# Komoran 객체 생성하기
#
# 이제, 형태소 분석을 위한 `Komoran` 객체를 생성합니다.
# 이 과정에서 Java 버전의 KOMORAN을 불러오게 되며, 약간의 시간이 소요됩니다. 이제 `Komoran` 객체의 메소드를 이용하여 형태소를 분석할 수 있습니다.

komoran = Komoran()

# 형태소 분석하기
#
# PyKOMORAN은 KOMORAN에서 제공하는 다양한 형태의 형태소 분석 결과를 제공합니다.
# 우선 입력 문장을 형태소 별로 나누어 `형태소/품사` 형태로 태깅된 결과를 보도록 하겠습니다.

print(komoran.get_plain_text("KOMORAN은 한국어 형태소 분석기입니다."))

# 형태소 분석의 결과인 품사 기호는 [품사표 (PoS Table)](https://docs.komoran.kr/firststep/postypes.html) 에서 찾아보실 수 있습니다.

#
# 번외편. 다양한 방법으로 형태소 분석하기
#
# `Komoran` 객체는 위에서 살펴본 `get_plain_text()` 메소드 외에도, 다양한 메소드들을 지원합니다.
# 분석할 문장을 준비하고, 위에서 생성한 `Komoran` 객체의 사용 예시를 살펴보겠습니다.

str_to_analyze = "① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."

# `get_nouns(str)`: 입력 문장에서 명사만 추출합니다.
print(komoran.get_nouns(str_to_analyze))

# `get_morphes_by_tags(str, tag_list=list)`: 입력 문장에서 주어진 품사들만 추출합니다.
print(komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', 'NNG', 'SF']))

# `get_plain_text(str)`: 입력 문장 내에 형태소/품사 형태로 태그를 합니다.
print(komoran.get_plain_text(str_to_analyze))

# `get_token_list(str)`: 입력 문장에 대해서 형태소/품사/시작지점/종료지점을 갖는 Token 자료형들을 반환받습니다.
print(komoran.get_token_list(str_to_analyze))

# `get_token_list(str, flatten=False)`: 입력 문장에 대해서 Token 자료형들을 반환받습니다. 이 때, 어절 단위로 나누어 반환받습니다.
print(komoran.get_token_list(str_to_analyze, flatten=False))

# `get_token_list(str, flatten=False, use_pos_name=True)`: 입력 문장에 대해서 Token 자료형들을 반환받습니다. 이 때, 품사 기호 대신 이름을 사용합니다.
print(komoran.get_token_list(str_to_analyze, use_pos_name=True))

# `get_list(str)`: 입력 문장에 대해서 형태소/품사를 갖는 Pair 자료형들을 반환받습니다.
print(komoran.get_list(str_to_analyze))

#
# 결론
#
# 지금까지 PyKomoran을 이용하여 3줄의 코드로 형태소 분석을 따라해보았습니다.
# 이 내용은 [PyKOMORAN 문서 사이트](https://docs.komoran.kr/pykomoran/tutorial.html)에서도 확인하실 수 있습니다.
