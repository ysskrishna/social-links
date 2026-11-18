"""Real public handles for the 1.5.0 platforms.

Each row is a profile URL taken from a public page (Wayback Machine captures with HTTP 200,
Wikidata identifiers, or a public page found by web search) and checked with a plain GET
when the site allows it. The comment on each row names the source and the live result.

Row: (platform, url, sanitized, bare_id). bare_id is None where the id is not accepted bare.
"""

import pytest

from sociallinks.core import SocialLinks


@pytest.fixture
def sl():
    return SocialLinks()


REAL_HANDLES = [
    # ---- part 1 ----
    # Hugging Face
    ('huggingface', 'https://huggingface.co/k00', 'https://huggingface.co/k00', 'k00'),  # wayback-200; live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/s-maddrellmander', 'https://huggingface.co/s-maddrellmander', 's-maddrellmander'),  # wayback-200; live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/m-a-coles', 'https://huggingface.co/m-a-coles', 'm-a-coles'),  # wayback-200; live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/M-A-D', 'https://huggingface.co/M-A-D', 'M-A-D'),  # wayback-200; live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/sbb', 'https://huggingface.co/sbb', 'sbb'),  # wikidata:P12201 (Berlin State Library); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/aymm', 'https://huggingface.co/aymm', 'aymm'),  # wikidata:P12201 (Angelina McMillan-Major); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/iizy', 'https://huggingface.co/iizy', 'iizy'),  # wikidata:P12201 (CalcFi); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/a0a7', 'https://huggingface.co/a0a7', 'a0a7'),  # wikidata:P12201 (Alexander Weimer); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/apple', 'https://huggingface.co/apple', 'apple'),  # wikidata:P12201 (Apple Inc.); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/gwern', 'https://huggingface.co/gwern', 'gwern'),  # wikidata:P12201 (Gwern Branwen); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/taide', 'https://huggingface.co/taide', 'taide'),  # wikidata:P12201 (Trustworthy AI Dialog Engine); live 200 (unknown ids 404)
    ('huggingface', 'https://huggingface.co/ogtal', 'https://huggingface.co/ogtal', 'ogtal'),  # wikidata:P12201 (Analysis & Numbers); live 200 (unknown ids 404)
    # Replicate
    ('replicate', 'https://replicate.com/kaarelkaarelson', 'https://replicate.com/kaarelkaarelson', 'kaarelkaarelson'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/m-834', 'https://replicate.com/m-834', 'm-834'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/m-kunz', 'https://replicate.com/m-kunz', 'm-kunz'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/m0hc3n', 'https://replicate.com/m0hc3n', 'm0hc3n'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/k-amir', 'https://replicate.com/k-amir', 'k-amir'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/s76354m', 'https://replicate.com/s76354m', 's76354m'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/saeed3e', 'https://replicate.com/saeed3e', 'saeed3e'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/sagolab', 'https://replicate.com/sagolab', 'sagolab'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/sai88uk', 'https://replicate.com/sai88uk', 'sai88uk'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/k1ng4rt', 'https://replicate.com/k1ng4rt', 'k1ng4rt'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/m1guelpf', 'https://replicate.com/m1guelpf', 'm1guelpf'),  # wayback-200; live 200 (unknown ids 404)
    ('replicate', 'https://replicate.com/sabuhigr', 'https://replicate.com/sabuhigr', 'sabuhigr'),  # wayback-200; live 200 (unknown ids 404)
    # ClawHub
    ('clawhub', 'https://clawhub.ai/1kalin', 'https://clawhub.ai/1kalin', '1kalin'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/mag3nt', 'https://clawhub.ai/mag3nt', 'mag3nt'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/sanool', 'https://clawhub.ai/sanool', 'sanool'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/k0nkupa', 'https://clawhub.ai/k0nkupa', 'k0nkupa'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/madsmith', 'https://clawhub.ai/madsmith', 'madsmith'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/salmonrk', 'https://clawhub.ai/salmonrk', 'salmonrk'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/keepchen', 'https://clawhub.ai/keepchen', 'keepchen'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://www.clawhub.ai/management', 'https://clawhub.ai/management', 'management'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/kissmyabs32', 'https://clawhub.ai/kissmyabs32', 'kissmyabs32'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/karthidreamr', 'https://clawhub.ai/karthidreamr', 'karthidreamr'),  # wayback-200; live 200 (unknown ids 404)
    # Lobsters
    ('lobsters', 'https://lobste.rs/~0', 'https://lobste.rs/~0', '0'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~7tehdt3cnw6kir6o', 'https://lobste.rs/~7tehdt3cnw6kir6o', '7tehdt3cnw6kir6o'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~2-D', 'https://lobste.rs/~2-D', '2-D'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~0x_asm', 'https://lobste.rs/~0x_asm', '0x_asm'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~0000', 'https://lobste.rs/~0000', '0000'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~01walid', 'https://lobste.rs/~01walid', '01walid'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~0x414A', 'https://lobste.rs/~0x414A', '0x414A'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~1', 'https://lobste.rs/~1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~2', 'https://lobste.rs/~2', '2'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~8', 'https://lobste.rs/~8', '8'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~a', 'https://lobste.rs/~a', 'a'),  # wayback-200; live 200 (unknown ids 404)
    ('lobsters', 'https://lobste.rs/~m', 'https://lobste.rs/~m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    # AtCoder
    ('atcoder', 'https://atcoder.jp/users/121', 'https://atcoder.jp/users/121', '121'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/0930_songzhiyu', 'https://atcoder.jp/users/0930_songzhiyu', '0930_songzhiyu'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/1424260058', 'https://atcoder.jp/users/1424260058', '1424260058'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/1Ac27', 'https://atcoder.jp/users/1Ac27', '1Ac27'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/4O4', 'https://atcoder.jp/users/4O4', '4O4'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/A0I', 'https://atcoder.jp/users/A0I', 'A0I'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/a0k', 'https://atcoder.jp/users/a0k', 'a0k'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/a1i', 'https://atcoder.jp/users/a1i', 'a1i'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/A29', 'https://atcoder.jp/users/A29', 'A29'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/0511hjb', 'https://atcoder.jp/users/0511hjb', '0511hjb'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/1_no_se', 'https://atcoder.jp/users/1_no_se', '1_no_se'),  # wayback-200; live 200 (unknown ids 404)
    ('atcoder', 'https://atcoder.jp/users/2023ljd', 'https://atcoder.jp/users/2023ljd', '2023ljd'),  # wayback-200; live 200 (unknown ids 404)
    # CodeChef
    ('codechef', 'https://www.codechef.com/users/a', 'https://www.codechef.com/users/a', 'a'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/s.max', 'https://www.codechef.com/users/s.max', 's.max'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/13151-1', 'https://www.codechef.com/users/13151-1', '13151-1'),  # wayback-200; live 200
    ('codechef', 'https://www.codechef.com/users/22445', 'https://www.codechef.com/users/22445', '22445'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/07EE37', 'https://www.codechef.com/users/07EE37', '07EE37'),  # wayback-200; live 200
    ('codechef', 'https://www.codechef.com/users/s', 'https://www.codechef.com/users/s', 's'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/s2n', 'https://www.codechef.com/users/s2n', 's2n'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/91as', 'https://www.codechef.com/users/91as', '91as'),  # wayback-200; live 200
    ('codechef', 'https://www.codechef.com/users/a000', 'https://www.codechef.com/users/a000', 'a000'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/a001', 'https://www.codechef.com/users/a001', 'a001'),  # wayback-200; live 200
    ('codechef', 'http://www.codechef.com/users/_arjun', 'https://www.codechef.com/users/_arjun', '_arjun'),  # wayback-200; live 404
    ('codechef', 'http://www.codechef.com/users/3rdEye', 'https://www.codechef.com/users/3rdEye', '3rdEye'),  # wayback-200; live 404
    # Topcoder
    ('topcoder', 'https://profiles.topcoder.com/2rf', 'https://profiles.topcoder.com/2rf', '2rf'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/_Ties_And_Whys_', 'https://profiles.topcoder.com/_Ties_And_Whys_', '_Ties_And_Whys_'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/A.Araghian', 'https://profiles.topcoder.com/A.Araghian', 'A.Araghian'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/-XraY-', 'https://profiles.topcoder.com/-XraY-', '-XraY-'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/__math', 'https://profiles.topcoder.com/__math', '__math'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/1849285087', 'https://profiles.topcoder.com/1849285087', '1849285087'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/0moikane', 'https://profiles.topcoder.com/0moikane', '0moikane'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/2PaVeL', 'https://profiles.topcoder.com/2PaVeL', '2PaVeL'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/a_u', 'https://profiles.topcoder.com/a_u', 'a_u'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/agh', 'https://profiles.topcoder.com/agh', 'agh'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/agw', 'https://profiles.topcoder.com/agw', 'agw'),  # wayback-200; live 200
    ('topcoder', 'https://profiles.topcoder.com/cpy', 'https://profiles.topcoder.com/cpy', 'cpy'),  # wayback-200; live 200
    # TryHackMe
    ('tryhackme', 'https://tryhackme.com/p/%D0%90%D0%BA%D1%83%D0%BB%D0%B0%D0%B5%D0%B2%D0%B0%20%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B0%20%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%BD%D0%B0', 'https://tryhackme.com/p/%D0%90%D0%BA%D1%83%D0%BB%D0%B0%D0%B5%D0%B2%D0%B0%20%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B0%20%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%BD%D0%B0', '%D0%90%D0%BA%D1%83%D0%BB%D0%B0%D0%B5%D0%B2%D0%B0%20%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B0%20%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%BD%D0%B0'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/%E7%A5%90%E9%87%8C%E5%B2%A1', 'https://tryhackme.com/p/%E7%A5%90%E9%87%8C%E5%B2%A1', '%E7%A5%90%E9%87%8C%E5%B2%A1'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/727Zenshinyoroi', 'https://tryhackme.com/p/727Zenshinyoroi', '727Zenshinyoroi'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/..k1ngk0ng', 'https://tryhackme.com/p/..k1ngk0ng', '..k1ngk0ng'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/-', 'https://tryhackme.com/p/-', '-'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/_.kulzz._01', 'https://tryhackme.com/p/_.kulzz._01', '_.kulzz._01'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/0590406', 'https://tryhackme.com/p/0590406', '0590406'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/00JMB', 'https://tryhackme.com/p/00JMB', '00JMB'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/%D0%9F%D0%BE%D1%80%D0%B2%D0%B8%20%D1%8D%D1%82%D0%BE', 'https://tryhackme.com/p/%D0%9F%D0%BE%D1%80%D0%B2%D0%B8%20%D1%8D%D1%82%D0%BE', '%D0%9F%D0%BE%D1%80%D0%B2%D0%B8%20%D1%8D%D1%82%D0%BE'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/1', 'https://tryhackme.com/p/1', '1'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/a', 'https://tryhackme.com/p/a', 'a'),  # wayback-200; live check blocked (429)
    ('tryhackme', 'https://tryhackme.com/p/Kr', 'https://tryhackme.com/p/Kr', 'Kr'),  # wayback-200; live check blocked (429)
    # Qiita
    ('qiita', 'https://qiita.com/m-d', 'https://qiita.com/m-d', 'm-d'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/s-a-k-a-m-o-t-o', 'https://qiita.com/s-a-k-a-m-o-t-o', 's-a-k-a-m-o-t-o'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/m-009', 'https://qiita.com/m-009', 'm-009'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'http://qiita.com/K-1', 'https://qiita.com/K-1', 'K-1'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/s--s', 'https://qiita.com/s--s', 's--s'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/k--m', 'https://qiita.com/k--m', 'k--m'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'http://qiita.com/s-age', 'https://qiita.com/s-age', 's-age'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/K-029', 'https://qiita.com/K-029', 'K-029'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/m-ansa', 'https://qiita.com/m-ansa', 'm-ansa'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/m-260316', 'https://qiita.com/m-260316', 'm-260316'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/m-a-ple', 'https://qiita.com/m-a-ple', 'm-a-ple'),  # wayback-200; live 200 (unknown ids 404)
    ('qiita', 'https://qiita.com/m-agnet', 'https://qiita.com/m-agnet', 'm-agnet'),  # wayback-200; live 200 (unknown ids 404)
    # Habr
    ('habr', 'https://habr.com/users/027/', 'https://habr.com/users/027', '027'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/640509-040147/', 'https://habr.com/users/640509-040147', '640509-040147'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/32bit_me/', 'https://habr.com/users/32bit_me', '32bit_me'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/007913/', 'https://habr.com/users/007913', '007913'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/0ex0/', 'https://habr.com/users/0ex0', '0ex0'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/0Lexx0/', 'https://habr.com/users/0Lexx0', '0Lexx0'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/3ds/', 'https://habr.com/users/3ds', '3ds'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/3em/', 'https://habr.com/users/3em', '3em'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/411/', 'https://habr.com/users/411', '411'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/4p4/', 'https://habr.com/users/4p4', '4p4'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/a4k/', 'https://habr.com/users/a4k', 'a4k'),  # wayback-200; live 200 (unknown ids 404)
    ('habr', 'https://habr.com/users/a5b/', 'https://habr.com/users/a5b', 'a5b'),  # wayback-200; live 200 (unknown ids 404)
    # Zenn
    ('zenn', 'https://zenn.dev/m0a', 'https://zenn.dev/m0a', 'm0a'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/s0o_n0o', 'https://zenn.dev/s0o_n0o', 's0o_n0o'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/s13', 'https://zenn.dev/s13', 's13'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/m10e', 'https://zenn.dev/m10e', 'm10e'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/s0ar', 'https://zenn.dev/s0ar', 's0ar'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/s134', 'https://zenn.dev/s134', 's134'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/m0370', 'https://zenn.dev/m0370', 'm0370'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/m0m0i', 'https://zenn.dev/m0m0i', 'm0m0i'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/m10k1', 'https://zenn.dev/m10k1', 'm10k1'),  # wayback-200; live 200 (unknown ids 404)
    ('zenn', 'https://zenn.dev/s0nmy', 'https://zenn.dev/s0nmy', 's0nmy'),  # wayback-200; live 200 (unknown ids 404)
    # RubyGems
    ('rubygems', 'https://rubygems.org/profiles/1', 'https://rubygems.org/profiles/1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/maartenvanessen', 'https://rubygems.org/profiles/maartenvanessen', 'maartenvanessen'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/m-bucher', 'https://rubygems.org/profiles/m-bucher', 'm-bucher'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/1_', 'https://rubygems.org/profiles/1_', '1_'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'http://rubygems.org/profiles/1003', 'https://rubygems.org/profiles/1003', '1003'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/1_nhd500', 'https://rubygems.org/profiles/1_nhd500', '1_nhd500'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/MAABHAIRABI', 'https://rubygems.org/profiles/MAABHAIRABI', 'MAABHAIRABI'),  # wayback-200; live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/ko1', 'https://rubygems.org/profiles/ko1', 'ko1'),  # wikidata:P11533 (Koichi Sasada); live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/drbrain', 'https://rubygems.org/profiles/drbrain', 'drbrain'),  # wikidata:P11533 (Eric Hodel); live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/milouse', 'https://rubygems.org/profiles/milouse', 'milouse'),  # wikidata:P11533 (Étienne Deparis); live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/plizent', 'https://rubygems.org/profiles/plizent', 'plizent'),  # wikidata:P11533 (Plizent Foundation); live 200 (unknown ids 404)
    ('rubygems', 'https://rubygems.org/profiles/pragdave1', 'https://rubygems.org/profiles/pragdave1', 'pragdave1'),  # wikidata:P11533 (Dave Thomas); live 200 (unknown ids 404)
    # NuGet
    ('nuget', 'https://www.nuget.org/profiles/1ES', 'https://www.nuget.org/profiles/1ES', '1ES'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/7digital_content_dev', 'https://www.nuget.org/profiles/7digital_content_dev', '7digital_content_dev'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/1st.co', 'https://www.nuget.org/profiles/1st.co', '1st.co'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/1and1-beicher', 'https://www.nuget.org/profiles/1and1-beicher', '1and1-beicher'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/501st_alpha1', 'https://www.nuget.org/profiles/501st_alpha1', '501st_alpha1'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'http://www.nuget.org/profiles/1111111', 'https://www.nuget.org/profiles/1111111', '1111111'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/06needhamt', 'https://www.nuget.org/profiles/06needhamt', '06needhamt'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/0BLU', 'https://www.nuget.org/profiles/0BLU', '0BLU'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/1ma', 'https://www.nuget.org/profiles/1ma', '1ma'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/23W', 'https://www.nuget.org/profiles/23W', '23W'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/403', 'https://www.nuget.org/profiles/403', '403'),  # wayback-200; live 200 (unknown ids 404)
    ('nuget', 'https://www.nuget.org/profiles/4IR', 'https://www.nuget.org/profiles/4IR', '4IR'),  # wayback-200; live 200 (unknown ids 404)
    # SourceForge
    ('sourceforge', 'https://sourceforge.net/u/a0c/profile/', 'https://sourceforge.net/u/a0c/profile', 'a0c'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/a1a8468a9000aaa/profile/', 'https://sourceforge.net/u/a1a8468a9000aaa/profile', 'a1a8468a9000aaa'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'http://sourceforge.net/u/a-abuzaid/profile/', 'https://sourceforge.net/u/a-abuzaid/profile', 'a-abuzaid'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/a_alessandretti/profile/', 'https://sourceforge.net/u/a_alessandretti/profile', 'a_alessandretti'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/a12/profile/', 'https://sourceforge.net/u/a12/profile', 'a12'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'http://sourceforge.net/u/a1s/profile/', 'https://sourceforge.net/u/a1s/profile', 'a1s'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'http://sourceforge.net/u/a54/profile/', 'https://sourceforge.net/u/a54/profile', 'a54'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'http://sourceforge.net/u/a73/profile/', 'https://sourceforge.net/u/a73/profile', 'a73'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'http://sourceforge.net/u/a7x/profile/', 'https://sourceforge.net/u/a7x/profile', 'a7x'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/a_b/profile/', 'https://sourceforge.net/u/a_b/profile', 'a_b'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/a_d/profile/', 'https://sourceforge.net/u/a_d/profile', 'a_d'),  # wayback-200; live check blocked (403)
    ('sourceforge', 'https://sourceforge.net/u/aa0/profile/', 'https://sourceforge.net/u/aa0/profile', 'aa0'),  # wayback-200; live check blocked (403)
    # SourceHut
    ('sourcehut', 'https://sr.ht/~m1n/', 'https://sr.ht/~m1n', 'm1n'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~s-ol/', 'https://sr.ht/~s-ol', 's-ol'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~0xxx/', 'https://sr.ht/~0xxx', '0xxx'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~m15a/', 'https://sr.ht/~m15a', 'm15a'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~m15o/', 'https://sr.ht/~m15o', 'm15o'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~m3t4/', 'https://sr.ht/~m3t4', 'm3t4'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~m3dry/', 'https://sr.ht/~m3dry', 'm3dry'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~ma3ke/', 'https://sr.ht/~ma3ke', 'ma3ke'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~kabir/', 'https://sr.ht/~kabir', 'kabir'),  # wayback-200; live 200 (unknown ids 404)
    ('sourcehut', 'https://sr.ht/~maddox/', 'https://sr.ht/~maddox', 'maddox'),  # wayback-200; live 200 (unknown ids 404)
    # Stack Exchange
    ('stack_exchange', 'https://stackexchange.com/users/0/juipas-mdjuipas', 'https://stackexchange.com/users/0', '0'),  # wayback-200; live check blocked (403)
    ('stack_exchange', 'http://stackexchange.com/users/1', 'https://stackexchange.com/users/1', '1'),  # wayback-200; live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/346?tab=accounts', 'https://stackexchange.com/users/346', '346'),  # wikidata:P10212 (Andrew Kelley); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/7871?tab=accounts', 'https://stackexchange.com/users/7871', '7871'),  # wikidata:P10212 (Kent Beck); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/5473?tab=accounts', 'https://stackexchange.com/users/5473', '5473'),  # wikidata:P10212 (Brian D. Foy); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/4288?tab=accounts', 'https://stackexchange.com/users/4288', '4288'),  # wikidata:P10212 (Scott Hanselman); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/4368?tab=accounts', 'https://stackexchange.com/users/4368', '4368'),  # wikidata:P10212 (John Resig); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/6565?tab=accounts', 'https://stackexchange.com/users/6565', '6565'),  # wikidata:P10212 (Michel Rodriguez); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/4472?tab=accounts', 'https://stackexchange.com/users/4472', '4472'),  # wikidata:P10212 (Jeni Tennison); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/9211?tab=accounts', 'https://stackexchange.com/users/9211', '9211'),  # wikidata:P10212 (Miguel de Icaza); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/14748?tab=accounts', 'https://stackexchange.com/users/14748', '14748'),  # wikidata:P10212 (Wil Shipley); live check blocked (403)
    ('stack_exchange', 'https://stackexchange.com/users/35628?tab=accounts', 'https://stackexchange.com/users/35628', '35628'),  # wikidata:P10212 (Ceki Gülcü); live check blocked (403)
    # Google Scholar
    ('google_scholar', 'https://scholar.google.com/citations?user=&user=-CVsmqYAAAAJ', 'https://scholar.google.com/citations?user=-CVsmqYAAAAJ', '-CVsmqYAAAAJ'),  # wayback-200; live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=%20v8Fqz0wg_soC&user=v8Fqz0wg_soC', 'https://scholar.google.com/citations?user=v8Fqz0wg_soC', 'v8Fqz0wg_soC'),  # wayback-200; live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=&user=0jdOu7cAAAAJ', 'https://scholar.google.com/citations?user=0jdOu7cAAAAJ', '0jdOu7cAAAAJ'),  # wayback-200; live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=&user=1VSZZOAAAAAJ', 'https://scholar.google.com/citations?user=1VSZZOAAAAAJ', '1VSZZOAAAAAJ'),  # wayback-200; live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=7pAtrAQAAAAJ', 'https://scholar.google.com/citations?user=7pAtrAQAAAAJ', '7pAtrAQAAAAJ'),  # wikidata:P1960 (Marc Lewis); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=n42ww5sAAAAJ', 'https://scholar.google.com/citations?user=n42ww5sAAAAJ', 'n42ww5sAAAAJ'),  # wikidata:P1960 (Giuseppe Ghiani); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=hQD1wg8AAAAJ', 'https://scholar.google.com/citations?user=hQD1wg8AAAAJ', 'hQD1wg8AAAAJ'),  # wikidata:P1960 (Manish Kapoor); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=rXhXG6EAAAAJ', 'https://scholar.google.com/citations?user=rXhXG6EAAAAJ', 'rXhXG6EAAAAJ'),  # wikidata:P1960 (Abdul Ghani Razaqpur); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=xZROC_oAAAAJ', 'https://scholar.google.com/citations?user=xZROC_oAAAAJ', 'xZROC_oAAAAJ'),  # wikidata:P1960 (Andrew Pitman); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=YFMIRCYAAAAJ', 'https://scholar.google.com/citations?user=YFMIRCYAAAAJ', 'YFMIRCYAAAAJ'),  # wikidata:P1960 (Rami Hodrob); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=jGiFLP8AAAAJ', 'https://scholar.google.com/citations?user=jGiFLP8AAAAJ', 'jGiFLP8AAAAJ'),  # wikidata:P1960 (Chase Rainwater); live check blocked (403)
    ('google_scholar', 'https://scholar.google.com/citations?user=d91nymYAAAAJ', 'https://scholar.google.com/citations?user=d91nymYAAAAJ', 'd91nymYAAAAJ'),  # wikidata:P1960 (Eurico Wongo Gungula); live check blocked (403)
    # Kick
    ('kick', 'https://kick.com/m', 'https://kick.com/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('kick', 'https://kick.com/M00nlightRavens', 'https://kick.com/M00nlightRavens', 'M00nlightRavens'),  # wayback-200; live 200 (unknown ids 404)
    ('kick', 'https://kick.com/m-0mq', 'https://kick.com/m-0mq', 'm-0mq'),  # wayback-200; live 200 (unknown ids 404)
    ('kick', 'https://kick.com/m0e_tv', 'https://kick.com/m0e_tv', 'm0e_tv'),  # wayback-200; live 200 (unknown ids 404)
    ('kick', 'https://kick.com/6ix9ine', 'https://kick.com/6ix9ine', '6ix9ine'),  # wikidata:P13863 (6ix9ine); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/M00PY', 'https://kick.com/M00PY', 'M00PY'),  # wayback-200; live 200 (unknown ids 404)
    ('kick', 'https://kick.com/n3on', 'https://kick.com/n3on', 'n3on'),  # wikidata:P13863 (N3on); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/clix', 'https://kick.com/clix', 'clix'),  # wikidata:P13863 (Clix); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/felps', 'https://kick.com/felps', 'felps'),  # wikidata:P13863 (Felps); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/Hamzah', 'https://kick.com/Hamzah', 'Hamzah'),  # wikidata:P13863 (Hamzah Saadah); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/cookie', 'https://kick.com/cookie', 'cookie'),  # wikidata:P13863 (Cookie King); live 200 (unknown ids 404)
    ('kick', 'https://kick.com/m...', 'https://kick.com/m...', 'm...'),  # wayback-200; live 500
    # Stan Store
    ('stan_store', 'https://stan.store/S-O-W-BreakingBoxes', 'https://stan.store/S-O-W-BreakingBoxes', 'S-O-W-BreakingBoxes'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/SafRo', 'https://stan.store/SafRo', 'SafRo'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/k3mmg', 'https://stan.store/k3mmg', 'k3mmg'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/saanar?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZnRzaATqAFtwZG9mAmZkaWQWUMYJujOh0fib2LatI7Uci2lKDeR9C2V4dG4DYWVtAjExAHNydGMGYXBwX2lkDzEyNDAyNDU3NDI4NzQxNAABp1LI04d7EYgdh1_4J15MycQoDMwmD7Sv4mVOHUntQGM4gMU2s1tG7kgPQhf3_aem_vuAaVg39aH3AeZYJru9Q_g', 'https://stan.store/saanar', 'saanar'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/m0dizzl3', 'https://stan.store/m0dizzl3', 'm0dizzl3'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/mackenzieheflin', 'https://stan.store/mackenzieheflin', 'mackenzieheflin'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/madalynkeys_947', 'https://stan.store/madalynkeys_947', 'madalynkeys_947'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/MadisonBcap', 'https://stan.store/MadisonBcap', 'MadisonBcap'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/Magicbylo', 'https://stan.store/Magicbylo', 'Magicbylo'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/magicwithsage', 'https://stan.store/magicwithsage', 'magicwithsage'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/Sadeessourdough', 'https://stan.store/Sadeessourdough', 'Sadeessourdough'),  # wayback-200; live 200 (unknown ids 404)
    ('stan_store', 'https://stan.store/SAlexander', 'https://stan.store/SAlexander', 'SAlexander'),  # wayback-200; live 200 (unknown ids 404)
    # Farcaster
    ('farcaster', 'https://farcaster.xyz/0--', 'https://farcaster.xyz/0--', '0--'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/0487205048720504', 'https://farcaster.xyz/0487205048720504', '0487205048720504'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/0-x-8.eth', 'https://farcaster.xyz/0-x-8.eth', '0-x-8.eth'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/01-001', 'https://farcaster.xyz/01-001', '01-001'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/0006688', 'https://farcaster.xyz/0006688', '0006688'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/001gifted', 'https://farcaster.xyz/001gifted', '001gifted'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/m', 'https://farcaster.xyz/m', 'm'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/s', 'https://farcaster.xyz/s', 's'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/01', 'https://farcaster.xyz/01', '01'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/03', 'https://farcaster.xyz/03', '03'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/sa', 'https://farcaster.xyz/sa', 'sa'),  # wayback-200; live 200
    ('farcaster', 'https://farcaster.xyz/k1', 'https://farcaster.xyz/k1', 'k1'),  # wayback-200; live 200
    # Figma
    ('figma', 'https://www.figma.com/@001', 'https://www.figma.com/@001', '001'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@0037e7b6_5391_4', 'https://www.figma.com/@0037e7b6_5391_4', '0037e7b6_5391_4'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@0489220e_cb2a_4', 'https://www.figma.com/@0489220e_cb2a_4', '0489220e_cb2a_4'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@012', 'https://www.figma.com/@012', '012'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@001vinicius', 'https://www.figma.com/@001vinicius', '001vinicius'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@0xHab', 'https://www.figma.com/@0xHab', '0xHab'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@1', 'https://www.figma.com/@1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@2', 'https://www.figma.com/@2', '2'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@3', 'https://www.figma.com/@3', '3'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@M', 'https://www.figma.com/@M', 'M'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@11', 'https://www.figma.com/@11', '11'),  # wayback-200; live 200 (unknown ids 404)
    ('figma', 'https://www.figma.com/@19', 'https://www.figma.com/@19', '19'),  # wayback-200; live 200 (unknown ids 404)
    # Douban
    ('douban', 'http://www.douban.com/people/M/', 'https://www.douban.com/people/M', 'M'),  # wayback-200; live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/158459516/', 'https://www.douban.com/people/158459516', '158459516'),  # wikidata:P6450 (Bei Dao); live 200 (unknown ids 404)
    ('douban', 'http://www.douban.com/people/M-0130/', 'https://www.douban.com/people/M-0130', 'M-0130'),  # wayback-200; live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/wong2/', 'https://www.douban.com/people/wong2', 'wong2'),  # wikidata:P6450 (Wang Dàpéng); live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/denovo/', 'https://www.douban.com/people/denovo', 'denovo'),  # wikidata:P6450 (Xu Haiyan); live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/89793311/', 'https://www.douban.com/people/89793311', '89793311'),  # wikidata:P6450 (Ni Nanjie); live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/liuzhiyi/', 'https://www.douban.com/people/liuzhiyi', 'liuzhiyi'),  # wikidata:P6450 (Liu Zhiyi); live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/jialibodi/', 'https://www.douban.com/people/jialibodi', 'jialibodi'),  # wikidata:P6450 (Ma Boyong); live 200 (unknown ids 404)
    ('douban', 'http://www.douban.com/people/m-0212./', 'https://www.douban.com/people/m-0212.', 'm-0212.'),  # wayback-200; live 200 (unknown ids 404)
    ('douban', 'http://www.douban.com/people/m-cha/', 'https://www.douban.com/people/m-cha', 'm-cha'),  # wayback-200; live 200 (unknown ids 404)
    ('douban', 'https://www.douban.com/people/M-Dogg/', 'https://www.douban.com/people/M-Dogg', 'M-Dogg'),  # wayback-200; live 200 (unknown ids 404)
    ('douban', 'http://www.douban.com/people/M-EastGirl/', 'https://www.douban.com/people/M-EastGirl', 'M-EastGirl'),  # wayback-200; live 200 (unknown ids 404)
    # Topmate
    ('topmate', 'https://topmate.io/s', 'https://topmate.io/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/maang_jobs_prep', 'https://topmate.io/maang_jobs_prep', 'maang_jobs_prep'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/m_froez', 'https://topmate.io/m_froez', 'm_froez'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/12bitmedia', 'https://topmate.io/12bitmedia', '12bitmedia'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/k_g', 'https://topmate.io/k_g', 'k_g'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/macy', 'https://topmate.io/macy', 'macy'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/kara', 'https://topmate.io/kara', 'kara'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/karun', 'https://topmate.io/karun', 'karun'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/kamyab', 'https://topmate.io/kamyab', 'kamyab'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/madhugr', 'https://topmate.io/madhugr', 'madhugr'),  # wayback-200; live 200 (unknown ids 404)
    ('topmate', 'https://topmate.io/madhuhc', 'https://topmate.io/madhuhc', 'madhuhc'),  # wayback-200; live 200 (unknown ids 404)
    # Freelancer.com
    ('freelancer', 'https://www.freelancer.com/u/M', 'https://www.freelancer.com/u/M', 'M'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'http://www.freelancer.com/u/M0hammad0sman.html?', 'https://www.freelancer.com/u/M0hammad0sman.html', 'M0hammad0sman.html'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'http://www.freelancer.com/u/m00d.html', 'https://www.freelancer.com/u/m00d.html', 'm00d.html'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/K', 'https://www.freelancer.com/u/K', 'K'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/K8', 'https://www.freelancer.com/u/K8', 'K8'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/m00', 'https://www.freelancer.com/u/m00', 'm00'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/m06', 'https://www.freelancer.com/u/m06', 'm06'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/m2d', 'https://www.freelancer.com/u/m2d', 'm2d'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/K7g', 'https://www.freelancer.com/u/K7g', 'K7g'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/m00g', 'https://www.freelancer.com/u/m00g', 'm00g'),  # wayback-200; live 200 (unknown ids 404)
    ('freelancer', 'https://www.freelancer.com/u/M077', 'https://www.freelancer.com/u/M077', 'M077'),  # wayback-200; live 200 (unknown ids 404)
    # eBay
    ('ebay', 'https://www.ebay.com/usr/m', 'https://www.ebay.com/usr/m', 'm'),  # wayback-200; live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/m-a-p-sportscards', 'https://www.ebay.com/usr/m-a-p-sportscards', 'm-a-p-sportscards'),  # wayback-200; live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/m-and-a_sales.llc', 'https://www.ebay.com/usr/m-and-a_sales.llc', 'm-and-a_sales.llc'),  # wayback-200; live check blocked (403)
    ('ebay', 'http://www.ebay.com/usr/m-', 'https://www.ebay.com/usr/m-', 'm-'),  # wayback-200; live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/m-39570480_4', 'https://www.ebay.com/usr/m-39570480_4', 'm-39570480_4'),  # wayback-200; live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/155245502568', 'https://www.ebay.com/usr/155245502568', '155245502568'),  # wikidata:P7590 (Max Harwood); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/BullseyeSB', 'https://www.ebay.com/usr/BullseyeSB', 'BullseyeSB'),  # wikidata:P7590 (Bullseye Sneaker Boutique); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/it-velz', 'https://www.ebay.com/usr/it-velz', 'it-velz'),  # wikidata:P7590 (Velz); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/thelucid', 'https://www.ebay.com/usr/thelucid', 'thelucid'),  # wikidata:P7590 (The Lucid); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/222400355', 'https://www.ebay.com/usr/222400355', '222400355'),  # wikidata:P7590 (Funeral of the Minstrel); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/211857978', 'https://www.ebay.com/usr/211857978', '211857978'),  # wikidata:P7590 (This House is Not for Sale); live check blocked (403)
    ('ebay', 'https://www.ebay.com/usr/nikfab_94', 'https://www.ebay.com/usr/nikfab_94', 'nikfab_94'),  # wikidata:P7590 (Nikita Fabris); live check blocked (403)
    # Poshmark
    ('poshmark', 'https://poshmark.com/closet/003', 'https://poshmark.com/closet/003', '003'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/000bellanova000', 'https://poshmark.com/closet/000bellanova000', '000bellanova000'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/00_lisa_00', 'https://poshmark.com/closet/00_lisa_00', '00_lisa_00'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/0000adeals0000', 'https://poshmark.com/closet/0000adeals0000', '0000adeals0000'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/004', 'https://poshmark.com/closet/004', '004'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/012', 'https://poshmark.com/closet/012', '012'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/s39', 'https://poshmark.com/closet/s39', 's39'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/k16', 'https://poshmark.com/closet/k16', 'k16'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'https://poshmark.com/closet/0072', 'https://poshmark.com/closet/0072', '0072'),  # wayback-200; live 200 (unknown ids 404)
    ('poshmark', 'http://poshmark.com/closet/0106', 'https://poshmark.com/closet/0106', '0106'),  # wayback-200; live 200 (unknown ids 404)
    # Civitai
    ('civitai', 'https://civitai.com/user/...', 'https://civitai.com/user/...', '...'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00000-2836159340.png', 'https://civitai.com/user/00000-2836159340.png', '00000-2836159340.png'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00000-6724368.png', 'https://civitai.com/user/00000-6724368.png', '00000-6724368.png'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00000-784072425.png', 'https://civitai.com/user/00000-784072425.png', '00000-784072425.png'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00009-1899967673_R.png', 'https://civitai.com/user/00009-1899967673_R.png', '00009-1899967673_R.png'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/0000002', 'https://civitai.com/user/0000002', '0000002'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00000.png', 'https://civitai.com/user/00000.png', '00000.png'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00131-3780510050-sampler-DPM-SDE-Karras-512x512-1.jpg', 'https://civitai.com/user/00131-3780510050-sampler-DPM-SDE-Karras-512x512-1.jpg', '00131-3780510050-sampler-DPM-SDE-Karras-512x512-1.jpg'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/m', 'https://civitai.com/user/m', 'm'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/0x', 'https://civitai.com/user/0x', '0x'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/k2', 'https://civitai.com/user/k2', 'k2'),  # wayback-200; live 200
    ('civitai', 'https://civitai.com/user/00a', 'https://civitai.com/user/00a', '00a'),  # wayback-200; live 200
    # OpenSea
    ('opensea', 'https://opensea.io/M', 'https://opensea.io/M', 'M'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/m-angelopoulos_artist', 'https://opensea.io/m-angelopoulos_artist', 'm-angelopoulos_artist'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/m1r1am.eth', 'https://opensea.io/m1r1am.eth', 'm1r1am.eth'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/m--p--o', 'https://opensea.io/m--p--o', 'm--p--o'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/M-Baloch_irani', 'https://opensea.io/M-Baloch_irani', 'M-Baloch_irani'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/M-0010110', 'https://opensea.io/M-0010110', 'M-0010110'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/S', 'https://opensea.io/S', 'S'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/k', 'https://opensea.io/k', 'k'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/m3', 'https://opensea.io/m3', 'm3'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/k_', 'https://opensea.io/k_', 'k_'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/M-R', 'https://opensea.io/M-R', 'M-R'),  # wayback-200; live 200
    ('opensea', 'https://opensea.io/s0f', 'https://opensea.io/s0f', 's0f'),  # wayback-200; live 200
    # Hey.xyz
    ('hey_xyz', 'https://hey.xyz/u/00-00-00-00-00-00-00-00-00', 'https://hey.xyz/u/00-00-00-00-00-00-00-00-00', '00-00-00-00-00-00-00-00-00'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0---0', 'https://hey.xyz/u/0---0', '0---0'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-_-_', 'https://hey.xyz/u/0-_-_', '0-_-_'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/00000', 'https://hey.xyz/u/00000', '00000'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-0-0-0', 'https://hey.xyz/u/0-0-0-0', '0-0-0-0'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/safe', 'https://hey.xyz/u/safe', 'safe'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-0-1', 'https://hey.xyz/u/0-0-1', '0-0-1'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-0-4', 'https://hey.xyz/u/0-0-4', '0-0-4'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-0-7', 'https://hey.xyz/u/0-0-7', '0-0-7'),  # wayback-200; live 200 (unknown ids 404)
    ('hey_xyz', 'https://hey.xyz/u/0-1-1', 'https://hey.xyz/u/0-1-1', '0-1-1'),  # wayback-200; live 200 (unknown ids 404)
    # Primal
    ('primal', 'https://primal.net/p/020f2d21ae09bf35fcdfb65decf1478b846f5f728ab30c5eaabcd6d081a81c3e', 'https://primal.net/p/020f2d21ae09bf35fcdfb65decf1478b846f5f728ab30c5eaabcd6d081a81c3e', None),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/04c915daefee38317fa734444acee390a8269fe5810b2241e5e6dd343dfbecc9', 'https://primal.net/p/04c915daefee38317fa734444acee390a8269fe5810b2241e5e6dd343dfbecc9', None),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q069z7m4uxczvx2kxyzmxal96ur0jgu3qxkx2vw84ht6hucktu0ssnuq7f', 'https://primal.net/p/npub1q069z7m4uxczvx2kxyzmxal96ur0jgu3qxkx2vw84ht6hucktu0ssnuq7f', 'npub1q069z7m4uxczvx2kxyzmxal96ur0jgu3qxkx2vw84ht6hucktu0ssnuq7f'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q0k5l5y437p48vlg4pynht5qkddgdzsea3r2dnxkpn2ju5kn993qnt7wtf', 'https://primal.net/p/npub1q0k5l5y437p48vlg4pynht5qkddgdzsea3r2dnxkpn2ju5kn993qnt7wtf', 'npub1q0k5l5y437p48vlg4pynht5qkddgdzsea3r2dnxkpn2ju5kn993qnt7wtf'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q0pauyces43zp2e0c2auvrj6fntdq9v0m2tk9mzd38ct8x6fx6xqsj5u4j', 'https://primal.net/p/npub1q0pauyces43zp2e0c2auvrj6fntdq9v0m2tk9mzd38ct8x6fx6xqsj5u4j', 'npub1q0pauyces43zp2e0c2auvrj6fntdq9v0m2tk9mzd38ct8x6fx6xqsj5u4j'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q2n02gqxtfnll09jpzmy8lkz89aezfje578df27pptrvtju75pcqu8a8k6', 'https://primal.net/p/npub1q2n02gqxtfnll09jpzmy8lkz89aezfje578df27pptrvtju75pcqu8a8k6', 'npub1q2n02gqxtfnll09jpzmy8lkz89aezfje578df27pptrvtju75pcqu8a8k6'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q2vlcmekwuyefptvsy2eqcqpnw5k2mwmy0wma2tq2qm0smcarlqsk3rx69', 'https://primal.net/p/npub1q2vlcmekwuyefptvsy2eqcqpnw5k2mwmy0wma2tq2qm0smcarlqsk3rx69', 'npub1q2vlcmekwuyefptvsy2eqcqpnw5k2mwmy0wma2tq2qm0smcarlqsk3rx69'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q33jywkl8r0e5g48lvrenxnr3lw59kzrw4e7p0cecslqzwc56eesjymqu0', 'https://primal.net/p/npub1q33jywkl8r0e5g48lvrenxnr3lw59kzrw4e7p0cecslqzwc56eesjymqu0', 'npub1q33jywkl8r0e5g48lvrenxnr3lw59kzrw4e7p0cecslqzwc56eesjymqu0'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q35eqc6rvdeejcwn47j0cgjp6mmxttx3yj3rlsvf43cy6a8y6zfq5mfg5m', 'https://primal.net/p/npub1q35eqc6rvdeejcwn47j0cgjp6mmxttx3yj3rlsvf43cy6a8y6zfq5mfg5m', 'npub1q35eqc6rvdeejcwn47j0cgjp6mmxttx3yj3rlsvf43cy6a8y6zfq5mfg5m'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q3dghm7yj78g62t7dqljtg4vf6r5vvqsvndfkkxflcnqk9ea6aksfkrpac', 'https://primal.net/p/npub1q3dghm7yj78g62t7dqljtg4vf6r5vvqsvndfkkxflcnqk9ea6aksfkrpac', 'npub1q3dghm7yj78g62t7dqljtg4vf6r5vvqsvndfkkxflcnqk9ea6aksfkrpac'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q3sle0kvfsehgsuexttt3ugjd8xdklxfwwkh559wxckmzddywnws6cd26p', 'https://primal.net/p/npub1q3sle0kvfsehgsuexttt3ugjd8xdklxfwwkh559wxckmzddywnws6cd26p', 'npub1q3sle0kvfsehgsuexttt3ugjd8xdklxfwwkh559wxckmzddywnws6cd26p'),  # wayback-200; live 200
    ('primal', 'https://primal.net/p/npub1q3t5ttqwjzjrv9q68twaj4t4ct4dg7mp8azjsu5rukqzlalan87s57u7l3', 'https://primal.net/p/npub1q3t5ttqwjzjrv9q68twaj4t4ct4dg7mp8azjsu5rukqzlalan87s57u7l3', 'npub1q3t5ttqwjzjrv9q68twaj4t4ct4dg7mp8azjsu5rukqzlalan87s57u7l3'),  # wayback-200; live 200
    # OpenStreetMap
    ('openstreetmap', 'http://www.openstreetmap.org/user/%21i%21', 'https://www.openstreetmap.org/user/%21i%21', '%21i%21'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/%C2%AB%D0%9C%D0%BE%D1%8F%20%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2%D1%8C%20%D0%BD%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%C2%BB', 'https://www.openstreetmap.org/user/%C2%AB%D0%9C%D0%BE%D1%8F%20%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2%D1%8C%20%D0%BD%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%C2%BB', '%C2%AB%D0%9C%D0%BE%D1%8F%20%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2%D1%8C%20%D0%BD%D0%B0%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%C2%BB'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/%C2%AB%D0%A1%D0%BC%D0%B0%D0%B9%D0%BB-%D0%94%D0%B5%D0%BD%D1%82%C2%BB', 'https://www.openstreetmap.org/user/%C2%AB%D0%A1%D0%BC%D0%B0%D0%B9%D0%BB-%D0%94%D0%B5%D0%BD%D1%82%C2%BB', '%C2%AB%D0%A1%D0%BC%D0%B0%D0%B9%D0%BB-%D0%94%D0%B5%D0%BD%D1%82%C2%BB'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/S%C3%A9ba_PRG', 'https://www.openstreetmap.org/user/S%C3%A9ba_PRG', 'S%C3%A9ba_PRG'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/%21MRGBoss', 'https://www.openstreetmap.org/user/%21MRGBoss', '%21MRGBoss'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'http://www.openstreetmap.org/user/k-1', 'https://www.openstreetmap.org/user/k-1', 'k-1'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/k-f', 'https://www.openstreetmap.org/user/k-f', 'k-f'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'http://www.openstreetmap.org/user/m%20c', 'https://www.openstreetmap.org/user/m%20c', 'm%20c'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/S%20T', 'https://www.openstreetmap.org/user/S%20T', 'S%20T'),  # wayback-200; live 200 (unknown ids 404)
    ('openstreetmap', 'https://www.openstreetmap.org/user/K-278', 'https://www.openstreetmap.org/user/K-278', 'K-278'),  # wayback-200; live 200 (unknown ids 404)
    # Pixelfed
    ('pixelfed', 'https://pixelfed.social/Sab', 'https://pixelfed.social/Sab', 'Sab'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/SahaHorriaFotografia', 'https://pixelfed.social/SahaHorriaFotografia', 'SahaHorriaFotografia'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/sadman.ca', 'https://pixelfed.social/sadman.ca', 'sadman.ca'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/Sandy-1a2b', 'https://pixelfed.social/Sandy-1a2b', 'Sandy-1a2b'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/s_pichi', 'https://pixelfed.social/s_pichi', 's_pichi'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/S8team', 'https://pixelfed.social/S8team', 'S8team'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/sai', 'https://pixelfed.social/sai', 'sai'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/sbb', 'https://pixelfed.social/sbb', 'sbb'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/kam', 'https://pixelfed.social/kam', 'kam'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/kch', 'https://pixelfed.social/kch', 'kch'),  # wayback-200; live 200 (unknown ids 404)
    ('pixelfed', 'https://pixelfed.social/kdj', 'https://pixelfed.social/kdj', 'kdj'),  # wayback-200; live 200 (unknown ids 404)
    # Misskey
    ('misskey', 'https://misskey.io/@010', 'https://misskey.io/@010', '010'),  # wayback-200; live 200
    ('misskey', 'http://misskey.io/@00nihs_369.atom', 'https://misskey.io/@00nihs_369.atom', '00nihs_369.atom'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@.maimai', 'https://misskey.io/@.maimai', '.maimai'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@00_saru', 'https://misskey.io/@00_saru', '00_saru'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@00029', 'https://misskey.io/@00029', '00029'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@000aoiro', 'https://misskey.io/@000aoiro', '000aoiro'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@006A66', 'https://misskey.io/@006A66', '006A66'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@m', 'https://misskey.io/@m', 'm'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@s', 'https://misskey.io/@s', 's'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@K', 'https://misskey.io/@K', 'K'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@0o', 'https://misskey.io/@0o', '0o'),  # wayback-200; live 200
    ('misskey', 'https://misskey.io/@0x', 'https://misskey.io/@0x', '0x'),  # wayback-200; live 200
    # Bilibili
    ('bilibili', 'https://space.bilibili.com/3494351363640156', 'https://space.bilibili.com/3494351363640156', '3494351363640156'),  # wikidata:P6455 (Z-Library); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/7966', 'https://space.bilibili.com/7966', '7966'),  # wikidata:P6455 (Hualing); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/3295', 'https://space.bilibili.com/3295', '3295'),  # wikidata:P6455 (Zhang Wei); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/8199', 'https://space.bilibili.com/8199', '8199'),  # wikidata:P6455 (Pan Min); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/43536', 'https://space.bilibili.com/43536', '43536'),  # wikidata:P6455 (Blackgoogle); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/11073', 'https://space.bilibili.com/11073', '11073'),  # wikidata:P6455 (Hanser); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/20709', 'https://space.bilibili.com/20709', '20709'),  # wikidata:P6455 (Ma Zhengyang); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/24377', 'https://space.bilibili.com/24377', '24377'),  # wikidata:P6455 (Alice Workshop); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/96541', 'https://space.bilibili.com/96541', '96541'),  # wikidata:P6455 (He Ruofan); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/329709', 'https://space.bilibili.com/329709', '329709'),  # wikidata:P6455 (Liu Zhixiao); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/122879', 'https://space.bilibili.com/122879', '122879'),  # wikidata:P6455 (Hawk Ao); live check blocked (412)
    ('bilibili', 'https://space.bilibili.com/433351', 'https://space.bilibili.com/433351', '433351'),  # wikidata:P6455 (Q28414510); live check blocked (412)
    # Letterboxd
    ('letterboxd', 'https://letterboxd.com/k0/', 'https://letterboxd.com/k0', 'k0'),  # wayback-200; live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/m00nag3daydr3am/', 'https://letterboxd.com/m00nag3daydr3am', 'm00nag3daydr3am'),  # wayback-200; live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/lee-sung-kyoung/', 'https://letterboxd.com/lee-sung-kyoung', 'lee-sung-kyoung'),  # wikidata:P12384 (Lee Sung-kyoung); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/m007_md/', 'https://letterboxd.com/m007_md', 'm007_md'),  # wayback-200; live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/4AD/', 'https://letterboxd.com/4AD', '4AD'),  # wikidata:P12384 (4AD); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/M00nshu/', 'https://letterboxd.com/M00nshu', 'M00nshu'),  # wayback-200; live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/KMF/', 'https://letterboxd.com/KMF', 'KMF'),  # wikidata:P12384 (Kleber Mendonça Filho); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/AFI/', 'https://letterboxd.com/AFI', 'AFI'),  # wikidata:P12384 (American Film Institute); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/BFI/', 'https://letterboxd.com/BFI', 'BFI'),  # wikidata:P12384 (British Film Institute); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/gff/', 'https://letterboxd.com/gff', 'gff'),  # wikidata:P12384 (Glasgow Film Festival); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/tubi/', 'https://letterboxd.com/tubi', 'tubi'),  # wikidata:P12384 (Tubi); live check blocked (403)
    ('letterboxd', 'https://letterboxd.com/imax/', 'https://letterboxd.com/imax', 'imax'),  # wikidata:P12384 (IMAX Corporation); live check blocked (403)
    # Goodreads
    ('goodreads', 'http://www.goodreads.com/user/show/1', 'https://www.goodreads.com/user/show/1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/2-odawg-diggity', 'https://www.goodreads.com/user/show/2', '2'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/3', 'https://www.goodreads.com/user/show/3', '3'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/5', 'https://www.goodreads.com/user/show/5', '5'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/6', 'https://www.goodreads.com/user/show/6', '6'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/7', 'https://www.goodreads.com/user/show/7', '7'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/8', 'https://www.goodreads.com/user/show/8', '8'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/9', 'https://www.goodreads.com/user/show/9', '9'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/20', 'https://www.goodreads.com/user/show/20', '20'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/30-jane', 'https://www.goodreads.com/user/show/30', '30'),  # wayback-200; live 200 (unknown ids 404)
    ('goodreads', 'http://www.goodreads.com/user/show/40', 'https://www.goodreads.com/user/show/40', '40'),  # wayback-200; live 200 (unknown ids 404)
    # Scratch
    ('scratch', 'https://scratch.mit.edu/users/---/', 'https://scratch.mit.edu/users/---', '---'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/---------------/', 'https://scratch.mit.edu/users/---------------', '---------------'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/----/', 'https://scratch.mit.edu/users/----', '----'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/-----------------0_0/', 'https://scratch.mit.edu/users/-----------------0_0', '-----------------0_0'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/-----------------R-/', 'https://scratch.mit.edu/users/-----------------R-', '-----------------R-'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'http://scratch.mit.edu/users/m--', 'https://scratch.mit.edu/users/m--', 'm--'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'http://scratch.mit.edu/users/M-16', 'https://scratch.mit.edu/users/M-16', 'M-16'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/M-29/', 'https://scratch.mit.edu/users/M-29', 'M-29'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'http://scratch.mit.edu/users/m-60', 'https://scratch.mit.edu/users/m-60', 'm-60'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/M-71/', 'https://scratch.mit.edu/users/M-71', 'M-71'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/m-9f/', 'https://scratch.mit.edu/users/m-9f', 'm-9f'),  # wayback-200; live 200 (unknown ids 404)
    ('scratch', 'https://scratch.mit.edu/users/m-AT/', 'https://scratch.mit.edu/users/m-AT', 'm-AT'),  # wayback-200; live 200 (unknown ids 404)
    # Discogs
    ('discogs', 'https://www.discogs.com/user/M-S', 'https://www.discogs.com/user/M-S', 'M-S'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/---ALLES___KAPOT---', 'https://www.discogs.com/user/---ALLES___KAPOT---', '---ALLES___KAPOT---'),  # wayback-200; live check blocked (403)
    ('discogs', 'https://www.discogs.com/user/---J.J.---', 'https://www.discogs.com/user/---J.J.---', '---J.J.---'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/----', 'https://www.discogs.com/user/----', '----'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/---Dj_Tom---', 'https://www.discogs.com/user/---Dj_Tom---', '---Dj_Tom---'),  # wayback-200; live check blocked (403)
    ('discogs', 'https://www.discogs.com/user/---Asterix---', 'https://www.discogs.com/user/---Asterix---', '---Asterix---'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/S', 'https://www.discogs.com/user/S', 'S'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/k', 'https://www.discogs.com/user/k', 'k'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/s.e', 'https://www.discogs.com/user/s.e', 's.e'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/k-2', 'https://www.discogs.com/user/k-2', 'k-2'),  # wayback-200; live check blocked (403)
    ('discogs', 'http://www.discogs.com/user/K-9', 'https://www.discogs.com/user/K-9', 'K-9'),  # wayback-200; live check blocked (403)
    ('discogs', 'https://www.discogs.com/user/K-B', 'https://www.discogs.com/user/K-B', 'K-B'),  # wayback-200; live check blocked (403)
    # MyAnimeList
    ('myanimelist', 'http://myanimelist.net/profile/M-', 'https://myanimelist.net/profile/M-', 'M-'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'http://myanimelist.net/profile/m-learning-guide', 'https://myanimelist.net/profile/m-learning-guide', 'm-learning-guide'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/M-5', 'https://myanimelist.net/profile/M-5', 'M-5'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/M-_', 'https://myanimelist.net/profile/M-_', 'M-_'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'http://myanimelist.net/profile/K', 'https://myanimelist.net/profile/K', 'K'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/M-E', 'https://myanimelist.net/profile/M-E', 'M-E'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'http://myanimelist.net/profile/M-H', 'https://myanimelist.net/profile/M-H', 'M-H'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/M-L', 'https://myanimelist.net/profile/M-L', 'M-L'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'http://myanimelist.net/profile/m-m', 'https://myanimelist.net/profile/m-m', 'm-m'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/M-V', 'https://myanimelist.net/profile/M-V', 'M-V'),  # wayback-200; live 200 (unknown ids 404)
    ('myanimelist', 'https://myanimelist.net/profile/s-c', 'https://myanimelist.net/profile/s-c', 's-c'),  # wayback-200; live 200 (unknown ids 404)
    # osu!
    ('osu', 'https://osu.ppy.sh/users/2', 'https://osu.ppy.sh/users/2', '2'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/10000', 'https://osu.ppy.sh/users/10000', '10000'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/3', 'https://osu.ppy.sh/users/3', '3'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/60', 'https://osu.ppy.sh/users/60', '60'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/400', 'https://osu.ppy.sh/users/400', '400'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/900', 'https://osu.ppy.sh/users/900', '900'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/5000', 'https://osu.ppy.sh/users/5000', '5000'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/6000', 'https://osu.ppy.sh/users/6000', '6000'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/7000', 'https://osu.ppy.sh/users/7000', '7000'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/8001', 'https://osu.ppy.sh/users/8001', '8001'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/60007', 'https://osu.ppy.sh/users/60007', '60007'),  # wayback-200; live 200 (unknown ids 404)
    ('osu', 'https://osu.ppy.sh/users/60012', 'https://osu.ppy.sh/users/60012', '60012'),  # wayback-200; live 200 (unknown ids 404)
    # itch.io
    ('itch_io', 'https://itch.io/profile/0-0sofiaguadalupe02', 'https://itch.io/profile/0-0sofiaguadalupe02', '0-0sofiaguadalupe02'),  # wayback-200; live 200 (unknown ids 404)
    ('itch_io', 'https://itch.io/profile/000000000', 'https://itch.io/profile/000000000', '000000000'),  # wayback-200; live 200 (unknown ids 404)
    ('itch_io', 'https://itch.io/profile/0-0-0-0-0-0', 'https://itch.io/profile/0-0-0-0-0-0', '0-0-0-0-0-0'),  # wayback-200; live 200 (unknown ids 404)
    ('itch_io', 'https://w.itch.io', 'https://itch.io/profile/w', 'w'),  # wikidata:P8176 (Anna Anthropy); live 200 (unknown ids 404)
    ('itch_io', 'https://4co.itch.io', 'https://itch.io/profile/4co', '4co'),  # wikidata:P8176 (4Co); live 200 (unknown ids 404)
    ('itch_io', 'https://aoq.itch.io', 'https://itch.io/profile/aoq', 'aoq'),  # wikidata:P8176 (Q133539961); live 200 (unknown ids 404)
    ('itch_io', 'https://dml.itch.io', 'https://itch.io/profile/dml', 'dml'),  # wikidata:P8176 (Jess Gates); live 200 (unknown ids 404)
    ('itch_io', 'https://cham.itch.io', 'https://itch.io/profile/cham', 'cham'),  # wikidata:P8176 (cham); live 200 (unknown ids 404)
    ('itch_io', 'https://atma.itch.io', 'https://itch.io/profile/atma', 'atma'),  # wikidata:P8176 (Atma Weapon); live 200 (unknown ids 404)
    ('itch_io', 'https://itch.io/profile/0-moosey-0', 'https://itch.io/profile/0-moosey-0', '0-moosey-0'),  # wayback-200; live 200 (unknown ids 404)
    ('itch_io', 'https://itch.io/profile/0-yoshi', 'https://itch.io/profile/0-yoshi', '0-yoshi'),  # wayback-200; live 200 (unknown ids 404)
    ('itch_io', 'https://itch.io/profile/00000livia', 'https://itch.io/profile/00000livia', '00000livia'),  # wayback-200; live 200 (unknown ids 404)
    # Speedrun.com
    ('speedrun', 'https://www.speedrun.com/users/-', 'https://www.speedrun.com/users/-', '-'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/-SoTS-SunSunFun', 'https://www.speedrun.com/users/-SoTS-SunSunFun', '-SoTS-SunSunFun'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/.1', 'https://www.speedrun.com/users/.1', '.1'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/--Q--DankNinja', 'https://www.speedrun.com/users/--Q--DankNinja', '--Q--DankNinja'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/-_-', 'https://www.speedrun.com/users/-_-', '-_-'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/0', 'https://www.speedrun.com/users/0', '0'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/--Q--Kraken', 'https://www.speedrun.com/users/--Q--Kraken', '--Q--Kraken'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/m', 'https://www.speedrun.com/users/m', 'm'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/k', 'https://www.speedrun.com/users/k', 'k'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/-7', 'https://www.speedrun.com/users/-7', '-7'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/-r', 'https://www.speedrun.com/users/-r', '-r'),  # wayback-200; live check blocked (403)
    ('speedrun', 'https://www.speedrun.com/users/M.', 'https://www.speedrun.com/users/M.', 'M.'),  # wayback-200; live check blocked (403)
    # Pixiv
    ('pixiv', 'https://www.pixiv.net/users/53823', 'https://www.pixiv.net/users/53823', '53823'),  # wikidata:P5435 (Michiro Ueyama); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/2323', 'https://www.pixiv.net/users/2323', '2323'),  # wikidata:P5435 (Toi8); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/7344', 'https://www.pixiv.net/users/7344', '7344'),  # wikidata:P5435 (Ichiharahikari Z); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/4228', 'https://www.pixiv.net/users/4228', '4228'),  # wikidata:P5435 (Chado); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/4733', 'https://www.pixiv.net/users/4733', '4733'),  # wikidata:P5435 (Heriyama); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/5483', 'https://www.pixiv.net/users/5483', '5483'),  # wikidata:P5435 (Mii Nekoi); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/5949', 'https://www.pixiv.net/users/5949', '5949'),  # wikidata:P5435 (Hiroshi Kanno); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/6728', 'https://www.pixiv.net/users/6728', '6728'),  # wikidata:P5435 (Hazuki Aikichi); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/3446', 'https://www.pixiv.net/users/3446', '3446'),  # wikidata:P5435 (redjuice); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/3881', 'https://www.pixiv.net/users/3881', '3881'),  # wikidata:P5435 (Yuka Nakajima); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/8940', 'https://www.pixiv.net/users/8940', '8940'),  # wikidata:P5435 (Ahndongshik); live check blocked (403)
    ('pixiv', 'https://www.pixiv.net/users/4595', 'https://www.pixiv.net/users/4595', '4595'),  # wikidata:P5435 (Sumiya); live check blocked (403)
    # Imgur
    ('imgur', 'http://imgur.com/user/M0000veBeeeeeech', 'https://imgur.com/user/M0000veBeeeeeech', 'M0000veBeeeeeech'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/.arrow', 'https://imgur.com/user/.arrow', '.arrow'),  # wayback-200; live 200
    ('imgur', 'https://imgur.com/user/s0ft_serve', 'https://imgur.com/user/s0ft_serve', 's0ft_serve'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/m00nGooSe', 'https://imgur.com/user/m00nGooSe', 'm00nGooSe'),  # wayback-200; live 200
    ('imgur', 'https://imgur.com/user/m00n', 'https://imgur.com/user/m00n', 'm00n'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/S0fa', 'https://imgur.com/user/S0fa', 'S0fa'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/s0ul', 'https://imgur.com/user/s0ul', 's0ul'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/S194', 'https://imgur.com/user/S194', 'S194'),  # wayback-200; live 200
    ('imgur', 'https://imgur.com/user/s1ka', 'https://imgur.com/user/s1ka', 's1ka'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/k00p', 'https://imgur.com/user/k00p', 'k00p'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/K0ff', 'https://imgur.com/user/K0ff', 'K0ff'),  # wayback-200; live 200
    ('imgur', 'http://imgur.com/user/k0pp', 'https://imgur.com/user/k0pp', 'k0pp'),  # wayback-200; live 200
    # Odysee
    ('odysee', 'https://odysee.com/@%C2%B0Heavenlyseal%E2%84%A2:4', 'https://odysee.com/@%C2%B0Heavenlyseal%E2%84%A2', '%C2%B0Heavenlyseal%E2%84%A2'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C5%81%C5%98B:5', 'https://odysee.com/@%C5%81%C5%98B', '%C5%81%C5%98B'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C3%81guilaDesier...', 'https://odysee.com/@%C3%81guilaDesier...', '%C3%81guilaDesier...'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C4%8Cesk%C3%BDLi..', 'https://odysee.com/@%C4%8Cesk%C3%BDLi..', '%C4%8Cesk%C3%BDLi..'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C3%89breszt-', 'https://odysee.com/@%C3%89breszt-', '%C3%89breszt-'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C3%89clairages_essentiels:8', 'https://odysee.com/@%C3%89clairages_essentiels', '%C3%89clairages_essentiels'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@%C3%81guilaDesierta:6', 'https://odysee.com/@%C3%81guilaDesierta', '%C3%81guilaDesierta'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@M', 'https://odysee.com/@M', 'M'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@S', 'https://odysee.com/@S', 'S'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@K', 'https://odysee.com/@K', 'K'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@M&', 'https://odysee.com/@M&', 'M&'),  # wayback-200; live 200
    ('odysee', 'https://odysee.com/@S..', 'https://odysee.com/@S..', 'S..'),  # wayback-200; live 200
    # GOG
    ('gog', 'https://www.gog.com/u/M-A', 'https://www.gog.com/u/M-A', 'M-A'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/m.a.durocher321', 'https://www.gog.com/u/m.a.durocher321', 'm.a.durocher321'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/M-ATTAX-18-', 'https://www.gog.com/u/M-ATTAX-18-', 'M-ATTAX-18-'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/m.r_lewis', 'https://www.gog.com/u/m.r_lewis', 'm.r_lewis'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/M-L-D', 'https://www.gog.com/u/M-L-D', 'M-L-D'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/m0', 'https://www.gog.com/u/m0', 'm0'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/m01', 'https://www.gog.com/u/m01', 'm01'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/M0f', 'https://www.gog.com/u/M0f', 'M0f'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/s3c', 'https://www.gog.com/u/s3c', 's3c'),  # wayback-200; live 200 (unknown ids 404)
    ('gog', 'https://www.gog.com/u/s_a', 'https://www.gog.com/u/s_a', 's_a'),  # wayback-200; live 200 (unknown ids 404)
    # Modrinth
    ('modrinth', 'https://modrinth.com/user/-M', 'https://modrinth.com/user/-M', '-M'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/-AlterVerseStudio-', 'https://modrinth.com/user/-AlterVerseStudio-', '-AlterVerseStudio-'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/.0x', 'https://modrinth.com/user/.0x', '.0x'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/---------', 'https://modrinth.com/user/---------', '---------'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/._.gabin', 'https://modrinth.com/user/._.gabin', '._.gabin'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/0', 'https://modrinth.com/user/0', '0'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/001damege', 'https://modrinth.com/user/001damege', '001damege'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/-ACE-', 'https://modrinth.com/user/-ACE-', '-ACE-'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/1', 'https://modrinth.com/user/1', '1'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/m', 'https://modrinth.com/user/m', 'm'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/k', 'https://modrinth.com/user/k', 'k'),  # wayback-200; live 200
    ('modrinth', 'https://modrinth.com/user/s6', 'https://modrinth.com/user/s6', 's6'),  # wayback-200; live 200
    # Niconico
    ('niconico', 'http://www.nicovideo.jp/user/1', 'https://www.nicovideo.jp/user/1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'http://www.nicovideo.jp/user/2', 'https://www.nicovideo.jp/user/2', '2'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'http://www.nicovideo.jp/user/3', 'https://www.nicovideo.jp/user/3', '3'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'http://www.nicovideo.jp/user/4', 'https://www.nicovideo.jp/user/4', '4'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/30', 'https://www.nicovideo.jp/user/30', '30'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'http://www.nicovideo.jp/user/10000', 'https://www.nicovideo.jp/user/10000', '10000'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/10000118', 'https://www.nicovideo.jp/user/10000118', '10000118'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/1000109?side_bar=bottom', 'https://www.nicovideo.jp/user/1000109', '1000109'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/2000015', 'https://www.nicovideo.jp/user/2000015', '2000015'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/20000995', 'https://www.nicovideo.jp/user/20000995', '20000995'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/20001393', 'https://www.nicovideo.jp/user/20001393', '20001393'),  # wayback-200; live 200 (unknown ids 404)
    ('niconico', 'https://www.nicovideo.jp/user/2000198?side_bar=top', 'https://www.nicovideo.jp/user/2000198', '2000198'),  # wayback-200; live 200 (unknown ids 404)
    # ---- part 2 ----
    # Roblox
    ('roblox', 'https://www.roblox.com/users/001/profile', 'https://www.roblox.com/users/001/profile', '001'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/0000000001/profile', 'https://www.roblox.com/users/0000000001/profile', '0000000001'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/01/profile', 'https://www.roblox.com/users/01/profile', '01'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/02/profile', 'https://www.roblox.com/users/02/profile', '02'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/03/profile', 'https://www.roblox.com/users/03/profile', '03'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/04152/profile', 'https://www.roblox.com/users/04152/profile', '04152'),  # wayback-200; live 200
    ('roblox', 'http://www.roblox.com/users/09283/profile', 'https://www.roblox.com/users/09283/profile', '09283'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/09368/profile/', 'https://www.roblox.com/users/09368/profile', '09368'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/000001/profile', 'https://www.roblox.com/users/000001/profile', '000001'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/000002/profile', 'https://www.roblox.com/users/000002/profile', '000002'),  # wayback-200; live 200
    ('roblox', 'https://www.roblox.com/users/000003/profile', 'https://www.roblox.com/users/000003/profile', '000003'),  # wayback-200; live 200
    ('roblox', 'http://www.roblox.com/users/01111/profile', 'https://www.roblox.com/users/01111/profile', '01111'),  # wayback-200; live 404
    # Truth Social
    ('truth_social', 'https://truthsocial.com/@m', 'https://truthsocial.com/@m', 'm'),  # wayback-200; live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@KatieBrittForAL', 'https://truthsocial.com/@KatieBrittForAL', 'KatieBrittForAL'),  # wikidata:P10858 (Katie Britt); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@K...', 'https://truthsocial.com/@K...', 'K...'),  # wayback-200; live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@K001_', 'https://truthsocial.com/@K001_', 'K001_'),  # wayback-200; live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@1819news', 'https://truthsocial.com/@1819news', '1819news'),  # wikidata:P10858 (1819 News); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@M0053', 'https://truthsocial.com/@M0053', 'M0053'),  # wayback-200; live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@NRA', 'https://truthsocial.com/@NRA', 'NRA'),  # wikidata:P10858 (National Rifle Association of America); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@VDH', 'https://truthsocial.com/@VDH', 'VDH'),  # wikidata:P10858 (Victor Davis Hanson); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@NRCC', 'https://truthsocial.com/@NRCC', 'NRCC'),  # wikidata:P10858 (National Republican Congressional Committee); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@cpac', 'https://truthsocial.com/@cpac', 'cpac'),  # wikidata:P10858 (Conservative Political Action Conference); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@nrlc', 'https://truthsocial.com/@nrlc', 'nrlc'),  # wikidata:P10858 (National Right to Life Committee); live check blocked (403)
    ('truth_social', 'https://truthsocial.com/@ACLJ', 'https://truthsocial.com/@ACLJ', 'ACLJ'),  # wikidata:P10858 (American Center for Law & Justice); live check blocked (403)
    # Buy Me a Coffee
    ('buymeacoffee', 'https://www.buymeacoffee.com/m', 'https://buymeacoffee.com/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('buymeacoffee', 'https://www.buymeacoffee.com/m.on.motherhood', 'https://buymeacoffee.com/m.on.motherhood', 'm.on.motherhood'),  # wayback-200; live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/m.10', 'https://buymeacoffee.com/m.10', 'm.10'),  # wayback-200; live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/m.igle_', 'https://buymeacoffee.com/m.igle_', 'm.igle_'),  # wayback-200; live 200 (unknown ids 404)
    ('buymeacoffee', 'https://www.buymeacoffee.com/M.19', 'https://buymeacoffee.com/M.19', 'M.19'),  # wayback-200; live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/aoq', 'https://buymeacoffee.com/aoq', 'aoq'),  # wikidata:P13981 (Attack on Quest); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/xstp', 'https://buymeacoffee.com/xstp', 'xstp'),  # wikidata:P13981 (Pepijn van der Stap); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/alovoa', 'https://buymeacoffee.com/alovoa', 'alovoa'),  # wikidata:P13981 (Q125392175); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/waterfox', 'https://buymeacoffee.com/waterfox', 'waterfox'),  # wikidata:P13981 (Waterfox); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/kavalerya', 'https://buymeacoffee.com/kavalerya', 'kavalerya'),  # wikidata:P13981 (Sergei Aslanyan); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/drjazdhill', 'https://buymeacoffee.com/drjazdhill', 'drjazdhill'),  # wikidata:P13981 (Jasmine D. Hill); live 200 (unknown ids 404)
    ('buymeacoffee', 'https://buymeacoffee.com/aniketsoni', 'https://buymeacoffee.com/aniketsoni', 'aniketsoni'),  # wikidata:P13981 (Aniket Abhishek Soni); live 200 (unknown ids 404)
    # Ko-fi
    ('ko_fi', 'https://ko-fi.com/tnt', 'https://ko-fi.com/tnt', 'tnt'),  # wikidata:P14695 (Q110242813); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/m00dynsfwprince', 'https://ko-fi.com/m00dynsfwprince', 'm00dynsfwprince'),  # wayback-200; live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/m00n_xx', 'https://ko-fi.com/m00n_xx', 'm00n_xx'),  # wayback-200; live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/itaku', 'https://ko-fi.com/itaku', 'itaku'),  # wikidata:P14695 (Itaku); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/yovska', 'https://ko-fi.com/yovska', 'yovska'),  # wikidata:P14695 (Yovska); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/aokiaku', 'https://ko-fi.com/aokiaku', 'aokiaku'),  # wikidata:P14695 (Q141533750); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/Z8Z36BHF', 'https://ko-fi.com/Z8Z36BHF', 'Z8Z36BHF'),  # wikidata:P14695 (Tedium); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/A6721DG1', 'https://ko-fi.com/A6721DG1', 'A6721DG1'),  # wikidata:P14695 (Adrienne Bazir); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/bakublep', 'https://ko-fi.com/bakublep', 'bakublep'),  # wikidata:P14695 (F-Craft); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/K3K42ME8W', 'https://ko-fi.com/K3K42ME8W', 'K3K42ME8W'),  # wikidata:P14695 (Cassetteboy); live 200 (unknown ids 404)
    ('ko_fi', 'https://ko-fi.com/N4N5JH2HD', 'https://ko-fi.com/N4N5JH2HD', 'N4N5JH2HD'),  # wikidata:P14695 (Q120065265); live 200 (unknown ids 404)
    # Last.fm
    ('lastfm', 'http://www.last.fm/user/M', 'https://www.last.fm/user/M', 'M'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/m-agicmurderbag', 'https://www.last.fm/user/m-agicmurderbag', 'm-agicmurderbag'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/M-.-n/', 'https://www.last.fm/user/M-.-n', 'M-.-n'),  # wayback-200; live 200
    ('lastfm', 'https://www.last.fm/user/m-', 'https://www.last.fm/user/m-', 'm-'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/m-15_03899/', 'https://www.last.fm/user/m-15_03899', 'm-15_03899'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/M--E--T--A--L/', 'https://www.last.fm/user/M--E--T--A--L', 'M--E--T--A--L'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/s', 'https://www.last.fm/user/s', 's'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/K/', 'https://www.last.fm/user/K', 'K'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/k-', 'https://www.last.fm/user/k-', 'k-'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/s-a/', 'https://www.last.fm/user/s-a', 's-a'),  # wayback-200; live 200
    ('lastfm', 'https://www.last.fm/user/k-7', 'https://www.last.fm/user/k-7', 'k-7'),  # wayback-200; live 200
    ('lastfm', 'http://www.last.fm/user/k-8', 'https://www.last.fm/user/k-8', 'k-8'),  # wayback-200; live 200
    # ORCID
    ('orcid', 'https://orcid.org/0000-0001-5069-3018', 'https://orcid.org/0000-0001-5069-3018', '0000-0001-5069-3018'),  # wikidata:P496 (Chris De Gruyter); live 200
    ('orcid', 'https://orcid.org/0000-0001-5238-7460', 'https://orcid.org/0000-0001-5238-7460', '0000-0001-5238-7460'),  # wikidata:P496 (Joseph John Scott); live 200
    ('orcid', 'https://orcid.org/0000-0001-5462-0086', 'https://orcid.org/0000-0001-5462-0086', '0000-0001-5462-0086'),  # wikidata:P496 (Christine E. Wilkinson); live 200
    ('orcid', 'https://orcid.org/0000-0001-6739-767X', 'https://orcid.org/0000-0001-6739-767X', '0000-0001-6739-767X'),  # wikidata:P496 (Alba Espargaró); live 200
    ('orcid', 'https://orcid.org/0000-0001-5514-6021', 'https://orcid.org/0000-0001-5514-6021', '0000-0001-5514-6021'),  # wikidata:P496 (Albert Kooistra); live 200
    ('orcid', 'https://orcid.org/0000-0001-5564-9788', 'https://orcid.org/0000-0001-5564-9788', '0000-0001-5564-9788'),  # wikidata:P496 (Mikael S Huhtala); live 200
    ('orcid', 'https://orcid.org/0000-0001-5693-1064', 'https://orcid.org/0000-0001-5693-1064', '0000-0001-5693-1064'),  # wikidata:P496 (Kevin Giles); live 200
    ('orcid', 'https://orcid.org/0000-0001-5801-1886', 'https://orcid.org/0000-0001-5801-1886', '0000-0001-5801-1886'),  # wikidata:P496 (Zohreh Zahedi); live 200
    ('orcid', 'https://orcid.org/0000-0001-5883-9034', 'https://orcid.org/0000-0001-5883-9034', '0000-0001-5883-9034'),  # wikidata:P496 (Celine Loddo); live 200
    ('orcid', 'https://orcid.org/0000-0001-5968-9795', 'https://orcid.org/0000-0001-5968-9795', '0000-0001-5968-9795'),  # wikidata:P496 (Sam Y Hong); live 200
    ('orcid', 'https://orcid.org/0000-0001-6133-9030', 'https://orcid.org/0000-0001-6133-9030', '0000-0001-6133-9030'),  # wikidata:P496 (Aslak Johansen); live 200
    ('orcid', 'https://orcid.org/0000-0001-6152-6127', 'https://orcid.org/0000-0001-6152-6127', '0000-0001-6152-6127'),  # wikidata:P496 (Ashish A Tamhane); live 200
    # npm
    ('npm', 'https://www.npmjs.com/~0', 'https://www.npmjs.com/~0', '0'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~007.surajit2023', 'https://www.npmjs.com/~007.surajit2023', '007.surajit2023'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~0xftm.eth', 'https://www.npmjs.com/~0xftm.eth', '0xftm.eth'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~-----', 'https://www.npmjs.com/~-----', '-----'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~002_zeleph', 'https://www.npmjs.com/~002_zeleph', '002_zeleph'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~01', 'https://www.npmjs.com/~01', '01'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~0-harshit-0', 'https://www.npmjs.com/~0-harshit-0', '0-harshit-0'),  # wayback-200; live check blocked (403)
    ('npm', 'https://www.npmjs.com/~swc', 'https://www.npmjs.com/~swc', 'swc'),  # wikidata:P11206 (swc); live check blocked (403)
    ('npm', 'https://www.npmjs.com/~turf', 'https://www.npmjs.com/~turf', 'turf'),  # wikidata:P11206 (Turf); live check blocked (403)
    ('npm', 'https://www.npmjs.com/~pnpm', 'https://www.npmjs.com/~pnpm', 'pnpm'),  # wikidata:P11206 (pnpm); live check blocked (403)
    ('npm', 'https://www.npmjs.com/~a0a7', 'https://www.npmjs.com/~a0a7', 'a0a7'),  # wikidata:P11206 (Alexander Weimer); live check blocked (403)
    ('npm', 'https://www.npmjs.com/~babel', 'https://www.npmjs.com/~babel', 'babel'),  # wikidata:P11206 (Babel); live check blocked (403)
    # Beacons
    ('beacons', 'https://beacons.ai/m', 'https://beacons.ai/m', 'm'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/m.e.myselfandfatigue', 'https://beacons.ai/m.e.myselfandfatigue', 'm.e.myselfandfatigue'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/m.a.d.c.j', 'https://beacons.ai/m.a.d.c.j', 'm.a.d.c.j'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/m.silva_oficial', 'https://beacons.ai/m.silva_oficial', 'm.silva_oficial'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/M.A.X', 'https://beacons.ai/M.A.X', 'M.A.X'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/k', 'https://beacons.ai/k', 'k'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/ma', 'https://beacons.ai/ma', 'ma'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/k9', 'https://beacons.ai/k9', 'k9'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/M3L', 'https://beacons.ai/M3L', 'M3L'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/m4i', 'https://beacons.ai/m4i', 'm4i'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/m_p', 'https://beacons.ai/m_p', 'm_p'),  # wayback-200; live check blocked (403)
    ('beacons', 'https://beacons.ai/s.h', 'https://beacons.ai/s.h', 's.h'),  # wayback-200; live check blocked (403)
    # Codeforces
    ('codeforces', 'http://www.codeforces.com/profile/---', 'https://codeforces.com/profile/---', '---'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/---------------', 'https://codeforces.com/profile/---------------', '---------------'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/-----_...--', 'https://codeforces.com/profile/-----_...--', '-----_...--'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/----', 'https://codeforces.com/profile/----', '----'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/---------__l__---------', 'https://codeforces.com/profile/---------__l__---------', '---------__l__---------'),  # wayback-200; live check blocked (403)
    ('codeforces', 'http://codeforces.com/profile/-----CUT-HERE-----', 'https://codeforces.com/profile/-----CUT-HERE-----', '-----CUT-HERE-----'),  # wayback-200; live check blocked (403)
    ('codeforces', 'http://codeforces.com/profile/--1', 'https://codeforces.com/profile/--1', '--1'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/--a', 'https://codeforces.com/profile/--a', '--a'),  # wayback-200; live check blocked (403)
    ('codeforces', 'http://www.codeforces.com/profile/--d', 'https://codeforces.com/profile/--d', '--d'),  # wayback-200; live check blocked (403)
    ('codeforces', 'http://codeforces.com/profile/-.-', 'https://codeforces.com/profile/-.-', '-.-'),  # wayback-200; live check blocked (403)
    ('codeforces', 'https://codeforces.com/profile/M-W', 'https://codeforces.com/profile/M-W', 'M-W'),  # wayback-200; live check blocked (403)
    ('codeforces', 'http://codeforces.com/profile/M.A', 'https://codeforces.com/profile/M.A', 'M.A'),  # wayback-200; live check blocked (403)
    # Codewars
    ('codewars', 'https://www.codewars.com/users/0DE', 'https://www.codewars.com/users/0DE', '0DE'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/501NotImplemented', 'https://www.codewars.com/users/501NotImplemented', '501NotImplemented'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/-Alex-', 'https://www.codewars.com/users/-Alex-', '-Alex-'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/m0__0n', 'https://www.codewars.com/users/m0__0n', 'm0__0n'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/111477', 'https://www.codewars.com/users/111477', '111477'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/0.5LiterBier', 'https://www.codewars.com/users/0.5LiterBier', '0.5LiterBier'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'http://www.codewars.com/users/1b8', 'https://www.codewars.com/users/1b8', '1b8'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/2EZ', 'https://www.codewars.com/users/2EZ', '2EZ'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/m99', 'https://www.codewars.com/users/m99', 'm99'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/-anony-mouse-', 'https://www.codewars.com/users/-anony-mouse-', '-anony-mouse-'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/0kaguya', 'https://www.codewars.com/users/0kaguya', '0kaguya'),  # wayback-200; live 200 (unknown ids 404)
    ('codewars', 'https://www.codewars.com/users/0xbba', 'https://www.codewars.com/users/0xbba', '0xbba'),  # wayback-200; live 200 (unknown ids 404)
    # Codeberg
    ('codeberg', 'https://codeberg.org/m', 'https://codeberg.org/m', 'm'),  # wayback-200; live check blocked (403)
    ('codeberg', 'https://codeberg.org/m-casanova.keys', 'https://codeberg.org/m-casanova.keys', 'm-casanova.keys'),  # wayback-200; live check blocked (403)
    ('codeberg', 'https://codeberg.org/m.kornienko', 'https://codeberg.org/m.kornienko', 'm.kornienko'),  # wayback-200; live check blocked (403)
    ('codeberg', 'https://codeberg.org/m-casanova', 'https://codeberg.org/m-casanova', 'm-casanova'),  # wayback-200; live check blocked (403)
    ('codeberg', 'https://codeberg.org/Peppermint_OS', 'https://codeberg.org/Peppermint_OS', 'Peppermint_OS'),  # wikidata:P12045 (Peppermint Linux OS); live check blocked (403)
    ('codeberg', 'https://codeberg.org/M0on9', 'https://codeberg.org/M0on9', 'M0on9'),  # wayback-200; live check blocked (403)
    ('codeberg', 'https://codeberg.org/mro', 'https://codeberg.org/mro', 'mro'),  # wikidata:P12045 (Marcus Rohrmoser); live check blocked (403)
    ('codeberg', 'https://codeberg.org/cfhn', 'https://codeberg.org/cfhn', 'cfhn'),  # wikidata:P12045 (Code for Heilbronn e.V.); live check blocked (403)
    ('codeberg', 'https://codeberg.org/bacs', 'https://codeberg.org/bacs', 'bacs'),  # wikidata:P12045 (Q137647967); live check blocked (403)
    ('codeberg', 'https://codeberg.org/jwyg', 'https://codeberg.org/jwyg', 'jwyg'),  # wikidata:P12045 (Jonathan W. Y. Gray); live check blocked (403)
    ('codeberg', 'https://codeberg.org/prav', 'https://codeberg.org/prav', 'prav'),  # wikidata:P12045 (The Prav Cooperative); live check blocked (403)
    ('codeberg', 'https://codeberg.org/ilai', 'https://codeberg.org/ilai', 'ilai'),  # wikidata:P12045 (Ilaï Deutel); live check blocked (403)
    # crates.io
    ('crates_io', 'https://crates.io/users/0cv', 'https://crates.io/users/0cv', '0cv'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/0-0-1', 'https://crates.io/users/0-0-1', '0-0-1'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/08820048', 'https://crates.io/users/08820048', '08820048'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/0-jake-0', 'https://crates.io/users/0-jake-0', '0-jake-0'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/38', 'https://crates.io/users/38', '38'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/52', 'https://crates.io/users/52', '52'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/64', 'https://crates.io/users/64', '64'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/71', 'https://crates.io/users/71', '71'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/0jg', 'https://crates.io/users/0jg', '0jg'),  # wayback-200; live 200 (unknown ids 404)
    ('crates_io', 'https://crates.io/users/102', 'https://crates.io/users/102', '102'),  # wayback-200; live 200 (unknown ids 404)
    # Gitee
    ('gitee', 'https://gitee.com/M', 'https://gitee.com/M', 'M'),  # wayback-200; live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/m-developer', 'https://gitee.com/m-developer', 'm-developer'),  # wayback-200; live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/m8oo_admin', 'https://gitee.com/m8oo_admin', 'm8oo_admin'),  # wayback-200; live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/M-Z-Q', 'https://gitee.com/M-Z-Q', 'M-Z-Q'),  # wayback-200; live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/gitea', 'https://gitee.com/gitea', 'gitea'),  # wikidata:P10884 (Gitea); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/sogou', 'https://gitee.com/sogou', 'sogou'),  # wikidata:P10884 (Sogou); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/LiteOS', 'https://gitee.com/LiteOS', 'LiteOS'),  # wikidata:P10884 (LiteOS); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/webank', 'https://gitee.com/webank', 'webank'),  # wikidata:P10884 (WeBank); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/Tencent', 'https://gitee.com/Tencent', 'Tencent'),  # wikidata:P10884 (Tencent); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/oschina', 'https://gitee.com/oschina', 'oschina'),  # wikidata:P10884 (OSChina); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/oceanbase', 'https://gitee.com/oceanbase', 'oceanbase'),  # wikidata:P10884 (OceanBase); live 200 (unknown ids 404)
    ('gitee', 'https://gitee.com/sa88sunnybainsgauravcom', 'https://gitee.com/sa88sunnybainsgauravcom', 'sa88sunnybainsgauravcom'),  # wayback-200; live check blocked (403)
    # Wattpad
    ('wattpad', 'https://www.wattpad.com/user/AuthorDianaNixon', 'https://www.wattpad.com/user/AuthorDianaNixon', 'AuthorDianaNixon'),  # web:websearch; live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/Ariana_Godoy', 'https://www.wattpad.com/user/Ariana_Godoy', 'Ariana_Godoy'),  # wikidata:P11637 (Ariana Godoy); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/WattpadFanfic', 'https://www.wattpad.com/user/WattpadFanfic', 'WattpadFanfic'),  # web:official genre profile; live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/zayn', 'https://www.wattpad.com/user/zayn', 'zayn'),  # wikidata:P11637 (Zayn Malik); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/Wineko', 'https://www.wattpad.com/user/Wineko', 'Wineko'),  # wikidata:P11637 (Wineko); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/vhaldai', 'https://www.wattpad.com/user/vhaldai', 'vhaldai'),  # wikidata:P11637 (Violeta Boyd); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/ElleEats', 'https://www.wattpad.com/user/ElleEats', 'ElleEats'),  # wikidata:P11637 (Elle John); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/CathyaMp', 'https://www.wattpad.com/user/CathyaMp', 'CathyaMp'),  # wikidata:P11637 (Cathya MP); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/BoggyFama', 'https://www.wattpad.com/user/BoggyFama', 'BoggyFama'),  # wikidata:P11637 (Eric Cochrane); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/NiNeGorman', 'https://www.wattpad.com/user/NiNeGorman', 'NiNeGorman'),  # wikidata:P11637 (Nine Gorman); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/BrianGjini', 'https://www.wattpad.com/user/BrianGjini', 'BrianGjini'),  # wikidata:P11637 (Q138677209); live 200 (unknown ids 404)
    ('wattpad', 'https://www.wattpad.com/user/SAVNichola', 'https://www.wattpad.com/user/SAVNichola', 'SAVNichola'),  # wikidata:P11637 (S.A.V. Nichola); live 200 (unknown ids 404)
    # AniList
    ('anilist', 'https://anilist.co/user/03s', 'https://anilist.co/user/03s', '03s'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/0YakumoKikuhiko0/', 'https://anilist.co/user/0YakumoKikuhiko0', '0YakumoKikuhiko0'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/000000/', 'https://anilist.co/user/000000', '000000'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/000Nawe', 'https://anilist.co/user/000Nawe', '000Nawe'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/002Epic/', 'https://anilist.co/user/002Epic', '002Epic'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/1', 'https://anilist.co/user/1', '1'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/M', 'https://anilist.co/user/M', 'M'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/s', 'https://anilist.co/user/s', 's'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/K', 'https://anilist.co/user/K', 'K'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/0o/', 'https://anilist.co/user/0o', '0o'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/S3/', 'https://anilist.co/user/S3', 'S3'),  # wayback-200; live 200
    ('anilist', 'https://anilist.co/user/0ak/', 'https://anilist.co/user/0ak', '0ak'),  # wayback-200; live 200
    # DeviantArt
    ('deviantart', 'https://www.deviantart.com/s/', 'https://www.deviantart.com/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/purrplecatmusic', 'https://www.deviantart.com/purrplecatmusic', 'purrplecatmusic'),  # wikidata:P7737 (Purrple Cat); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/s-', 'https://www.deviantart.com/s-', 's-'),  # wayback-200; live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/4649nadeshiko', 'https://www.deviantart.com/4649nadeshiko', '4649nadeshiko'),  # wikidata:P7737 (4649nadeshiko); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/JoelAmatGuell', 'https://www.deviantart.com/JoelAmatGuell', 'JoelAmatGuell'),  # wikidata:P7737 (Joel Amat Güell); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/peet', 'https://www.deviantart.com/peet', 'peet'),  # wikidata:P7737 (Peter Xavier Price); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/HDS7', 'https://www.deviantart.com/HDS7', 'HDS7'),  # wikidata:P7737 (Alexander Julien); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/cmcc', 'https://www.deviantart.com/cmcc', 'cmcc'),  # wikidata:P7737 (Craig McCracken); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/rbcp', 'https://www.deviantart.com/rbcp', 'rbcp'),  # wikidata:P7737 (Brad Carter); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/goor', 'https://www.deviantart.com/goor', 'goor'),  # wikidata:P7737 (Q136440199); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/k6ka', 'https://www.deviantart.com/k6ka', 'k6ka'),  # wikidata:P7737 (Enoch Leung); live 200 (unknown ids 404)
    ('deviantart', 'https://www.deviantart.com/pimmy', 'https://www.deviantart.com/pimmy', 'pimmy'),  # wikidata:P7737 (Pimmy); live 200 (unknown ids 404)
    # Pexels
    ('pexels', 'https://www.pexels.com/@007-lovers-1125813', 'https://www.pexels.com/@007-lovers-1125813', '007-lovers-1125813'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@-6t8', 'https://www.pexels.com/@-6t8', '-6t8'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@m_a-gom3a-1196704', 'https://www.pexels.com/@m_a-gom3a-1196704', 'm_a-gom3a-1196704'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@1000990', 'https://www.pexels.com/@1000990', '1000990'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@0-2340285', 'https://www.pexels.com/@0-2340285', '0-2340285'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@-sb-/', 'https://www.pexels.com/@-sb-', '-sb-'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@s1k0/', 'https://www.pexels.com/@s1k0', 's1k0'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@sa72/', 'https://www.pexels.com/@sa72', 'sa72'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@saad', 'https://www.pexels.com/@saad', 'saad'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@k23d', 'https://www.pexels.com/@k23d', 'k23d'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@kaan', 'https://www.pexels.com/@kaan', 'kaan'),  # wayback-200; live check blocked (403)
    ('pexels', 'https://www.pexels.com/@00eug/', 'https://www.pexels.com/@00eug', '00eug'),  # wayback-200; live check blocked (403)
    # Xiaohongshu (RedNote)
    ('xiaohongshu', 'http://www.rednote.com/user/profile/52d8c541b4c4d60e6c867480?xsec_token=ABh-QFQE3qx2YgIbuieE6DGO_otDp2UgJlqCzhqaLsEgI%3D&xsec_source=pc_note', 'https://www.rednote.com/user/profile/52d8c541b4c4d60e6c867480', '52d8c541b4c4d60e6c867480'),  # wayback-200; live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/6975432355', 'https://www.rednote.com/user/profile/6975432355', '6975432355'),  # wikidata:P12038 (Sangonomiya Kokomi); live 200
    ('xiaohongshu', 'https://www.rednote.com/user/profile/548272c8e779895e323f71d1', 'https://www.rednote.com/user/profile/548272c8e779895e323f71d1', '548272c8e779895e323f71d1'),  # wayback-200; live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/82vcwty74Pv', 'https://www.rednote.com/user/profile/82vcwty74Pv', '82vcwty74Pv'),  # wikidata:P12038 (Yuxin Cui); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/astagaco', 'https://www.rednote.com/user/profile/astagaco', 'astagaco'),  # wikidata:P12038 (astaga.co); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/952099593', 'https://www.rednote.com/user/profile/952099593', '952099593'),  # wikidata:P12038 (Gong Jun); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/Stevenkelly', 'https://www.rednote.com/user/profile/Stevenkelly', 'Stevenkelly'),  # wikidata:P12038 (Q108915168); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/prasaprasetya', 'https://www.rednote.com/user/profile/prasaprasetya', 'prasaprasetya'),  # wikidata:P12038 (Prasa Prasetya); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/5ba3563e43027f0001fa4b8d', 'https://www.rednote.com/user/profile/5ba3563e43027f0001fa4b8d', '5ba3563e43027f0001fa4b8d'),  # wikidata:P12038 (China Southern Airlines); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/5cd294b9000000001102dac2', 'https://www.rednote.com/user/profile/5cd294b9000000001102dac2', '5cd294b9000000001102dac2'),  # wikidata:P12038 (Dispatch); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/631072c1000000001200ea90', 'https://www.rednote.com/user/profile/631072c1000000001200ea90', '631072c1000000001200ea90'),  # wikidata:P12038 (Eurostar); live 200
    ('xiaohongshu', 'https://www.xiaohongshu.com/user/profile/63ff4a6b000000001f031ff1', 'https://www.rednote.com/user/profile/63ff4a6b000000001f031ff1', '63ff4a6b000000001f031ff1'),  # wikidata:P12038 (Kyushu Railway Company); live 200
    # Genius
    ('genius', 'https://genius.com/K-', 'https://genius.com/K-', 'K-'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/K-391-alan-walker-and-martin-tungevaag-play-sample', 'https://genius.com/K-391-alan-walker-and-martin-tungevaag-play-sample', 'K-391-alan-walker-and-martin-tungevaag-play-sample'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/K-391-and-rry-aurora-sample', 'https://genius.com/K-391-and-rry-aurora-sample', 'K-391-and-rry-aurora-sample'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/B-A_Monaie', 'https://genius.com/B-A_Monaie', 'B-A_Monaie'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/K-a-t-r-i-n-a-e', 'https://genius.com/K-a-t-r-i-n-a-e', 'K-a-t-r-i-n-a-e'),  # wayback-200; live check blocked (403)
    ('genius', 'http://genius.com/N-', 'https://genius.com/N-', 'N-'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/w-', 'https://genius.com/w-', 'w-'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/D-7', 'https://genius.com/D-7', 'D-7'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/k-be', 'https://genius.com/k-be', 'k-be'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/C---', 'https://genius.com/C---', 'C---'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/c-40', 'https://genius.com/c-40', 'c-40'),  # wayback-200; live check blocked (403)
    ('genius', 'https://genius.com/C-99', 'https://genius.com/C-99', 'C-99'),  # wayback-200; live check blocked (403)
    # Lemon8
    ('lemon8', 'https://www.lemon8-app.com/@....leavealoneme?region=us', 'https://www.lemon8-app.com/@....leavealoneme', '....leavealoneme'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@.....55539?region=th', 'https://www.lemon8-app.com/@.....55539', '.....55539'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@....lexi...._?region=us', 'https://www.lemon8-app.com/@....lexi...._', '....lexi...._'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@.4y98?region=us', 'https://www.lemon8-app.com/@.4y98', '.4y98'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@.bt99?region=th', 'https://www.lemon8-app.com/@.bt99', '.bt99'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@s0m_j?region=th', 'https://www.lemon8-app.com/@s0m_j', 's0m_j'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@k.ays?region=us', 'https://www.lemon8-app.com/@k.ays', 'k.ays'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@k.seq?region=us', 'https://www.lemon8-app.com/@k.seq', 'k.seq'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@...gsf?region=us', 'https://www.lemon8-app.com/@...gsf', '...gsf'),  # wayback-200; live 200 (unknown ids 404)
    ('lemon8', 'https://www.lemon8-app.com/@.10_98?region=th', 'https://www.lemon8-app.com/@.10_98', '.10_98'),  # wayback-200; live 200 (unknown ids 404)
    # Airbnb
    ('airbnb', 'http://airbnb.com/users/show/1', 'https://www.airbnb.com/users/show/1', '1'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/1000', 'https://www.airbnb.com/users/show/1000', '1000'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/1001', 'https://www.airbnb.com/users/show/1001', '1001'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/10006', 'https://www.airbnb.com/users/show/10006', '10006'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/10011', 'https://www.airbnb.com/users/show/10011', '10011'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100013', 'https://www.airbnb.com/users/show/100013', '100013'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100019', 'https://www.airbnb.com/users/show/100019', '100019'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100022', 'https://www.airbnb.com/users/show/100022', '100022'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100023', 'https://www.airbnb.com/users/show/100023', '100023'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100033', 'https://www.airbnb.com/users/show/100033', '100033'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100041', 'https://www.airbnb.com/users/show/100041', '100041'),  # wayback-200; live 200
    ('airbnb', 'http://www.airbnb.com/users/show/100046', 'https://www.airbnb.com/users/show/100046', '100046'),  # wayback-200; live 200
    # Trustpilot
    ('trustpilot', 'http://www.trustpilot.com/Users/1', 'https://www.trustpilot.com/users/1', '1'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'https://www.trustpilot.com/users/magic-link', 'https://www.trustpilot.com/users/magic-link', 'magic-link'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/users/1000017', 'https://www.trustpilot.com/users/1000017', '1000017'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/1012', 'https://www.trustpilot.com/users/1012', '1012'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/1014', 'https://www.trustpilot.com/users/1014', '1014'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/10003', 'https://www.trustpilot.com/users/10003', '10003'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/10041', 'https://www.trustpilot.com/users/10041', '10041'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/10114', 'https://www.trustpilot.com/users/10114', '10114'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/10127', 'https://www.trustpilot.com/users/10127', '10127'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/Users/10128', 'https://www.trustpilot.com/users/10128', '10128'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/users/100025', 'https://www.trustpilot.com/users/100025', '100025'),  # wayback-200; live check blocked (403)
    ('trustpilot', 'http://www.trustpilot.com/users/100034', 'https://www.trustpilot.com/users/100034', '100034'),  # wayback-200; live check blocked (403)
    # Carrd
    ('carrd', 'https://neverartistcommissions.carrd.co', 'https://neverartistcommissions.carrd.co', 'neverartistcommissions'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://rappaport-portfolio.carrd.co', 'https://rappaport-portfolio.carrd.co', 'rappaport-portfolio'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://toradh.carrd.co', 'https://toradh.carrd.co', 'toradh'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://chuwychu.carrd.co', 'https://chuwychu.carrd.co', 'chuwychu'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://manoslag.carrd.co', 'https://manoslag.carrd.co', 'manoslag'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://morphimus.carrd.co', 'https://morphimus.carrd.co', 'morphimus'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://raylinkhub.carrd.co', 'https://raylinkhub.carrd.co', 'raylinkhub'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://myportafolio.carrd.co', 'https://myportafolio.carrd.co', 'myportafolio'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://rayrattsportfolio.carrd.co', 'https://rayrattsportfolio.carrd.co', 'rayrattsportfolio'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://imaplatypusartcomms.carrd.co', 'https://imaplatypusartcomms.carrd.co', 'imaplatypusartcomms'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    ('carrd', 'https://reesieroospark-links.carrd.co', 'https://reesieroospark-links.carrd.co', 'reesieroospark-links'),  # web:websearch site:carrd.co; live 200 (unknown ids 404)
    # Blogger
    ('blogger', 'https://www.blogger.com/profile/01010075983544231080', 'https://www.blogger.com/profile/01010075983544231080', '01010075983544231080'),  # wikidata:P8772 (Flow); live 200
    ('blogger', 'https://www.blogger.com/profile/03248801212916411345', 'https://www.blogger.com/profile/03248801212916411345', '03248801212916411345'),  # wikidata:P8772 (Jason M. Pettus); live 200
    ('blogger', 'https://www.blogger.com/profile/10048510156143953896', 'https://www.blogger.com/profile/10048510156143953896', '10048510156143953896'),  # wikidata:P8772 (Titus Ikechukwu Nnabugwu); live 200
    ('blogger', 'https://www.blogger.com/profile/07199813303416083671', 'https://www.blogger.com/profile/07199813303416083671', '07199813303416083671'),  # wikidata:P8772 (Nick Redfern); live 200
    ('blogger', 'https://www.blogger.com/profile/03379103292621457026', 'https://www.blogger.com/profile/03379103292621457026', '03379103292621457026'),  # wikidata:P8772 (Peter M. Head); live 200
    ('blogger', 'https://www.blogger.com/profile/13829231169955265409', 'https://www.blogger.com/profile/13829231169955265409', '13829231169955265409'),  # wikidata:P8772 (John Kit Tang); live 200
    ('blogger', 'https://www.blogger.com/profile/17482934682589573414', 'https://www.blogger.com/profile/17482934682589573414', '17482934682589573414'),  # wikidata:P8772 (Robert Philip Bolton); live 200
    ('blogger', 'https://www.blogger.com/profile/11818671186074003777', 'https://www.blogger.com/profile/11818671186074003777', '11818671186074003777'),  # wikidata:P8772 (Peter Costantini); live 200
    ('blogger', 'https://www.blogger.com/profile/12372393717833610657', 'https://www.blogger.com/profile/12372393717833610657', '12372393717833610657'),  # wikidata:P8772 (Nicholas Stix); live 200
    ('blogger', 'https://www.blogger.com/profile/5836542', 'https://www.blogger.com/profile/5836542', '5836542'),  # wikidata:P8772 (Yoñlu); live 400
    ('blogger', 'https://www.blogger.com/profile/5160427648497943080', 'https://www.blogger.com/profile/5160427648497943080', '5160427648497943080'),  # wikidata:P8772 (Morgan McGuire); live 400
    ('blogger', 'https://www.blogger.com/profile/5202005598266553853', 'https://www.blogger.com/profile/5202005598266553853', '5202005598266553853'),  # wikidata:P8772 (Romanifolkets Kulturforening); live 400
    # Tistory
    ('tistory', 'https://dog-happy-coding.tistory.com', 'https://dog-happy-coding.tistory.com', 'dog-happy-coding'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://hi-hyuny.tistory.com', 'https://hi-hyuny.tistory.com', 'hi-hyuny'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'http://www2.tistory.com/', 'https://www2.tistory.com', 'www2'),  # wayback-200; live 200 (unknown ids 404)
    ('tistory', 'http://www9.tistory.com/', 'https://www9.tistory.com', 'www9'),  # wayback-200; live 200 (unknown ids 404)
    ('tistory', 'http://www22.tistory.com/', 'https://www22.tistory.com', 'www22'),  # wayback-200; live 200 (unknown ids 404)
    ('tistory', 'https://alias007.tistory.com', 'https://alias007.tistory.com', 'alias007'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://note8381.tistory.com', 'https://note8381.tistory.com', 'note8381'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://bluebada.tistory.com', 'https://bluebada.tistory.com', 'bluebada'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://chansman.tistory.com', 'https://chansman.tistory.com', 'chansman'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://sarywhere.tistory.com', 'https://sarywhere.tistory.com', 'sarywhere'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://javaexpert.tistory.com', 'https://javaexpert.tistory.com', 'javaexpert'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    ('tistory', 'https://monicareport.tistory.com', 'https://monicareport.tistory.com', 'monicareport'),  # web:websearch site:tistory.com; live 200 (unknown ids 404)
    # Untappd
    ('untappd', 'https://untappd.com/user/--', 'https://untappd.com/user/--', '--'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/-BeardedSpartan-', 'https://untappd.com/user/-BeardedSpartan-', '-BeardedSpartan-'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/---GIRD---', 'https://untappd.com/user/---GIRD---', '---GIRD---'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/-_billy_-', 'https://untappd.com/user/-_billy_-', '-_billy_-'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/--Asteria--', 'https://untappd.com/user/--Asteria--', '--Asteria--'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/-1X', 'https://untappd.com/user/-1X', '-1X'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/-C-', 'https://untappd.com/user/-C-', '-C-'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/-Cn', 'https://untappd.com/user/-Cn', '-Cn'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/M-A', 'https://untappd.com/user/M-A', 'M-A'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/M-G', 'https://untappd.com/user/M-G', 'M-G'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/s-9', 'https://untappd.com/user/s-9', 's-9'),  # wayback-200; live check blocked (403)
    ('untappd', 'https://untappd.com/user/S-F', 'https://untappd.com/user/S-F', 'S-F'),  # wayback-200; live check blocked (403)
    # The StoryGraph
    ('storygraph', 'https://app.thestorygraph.com/profile/2wn', 'https://app.thestorygraph.com/profile/2wn', '2wn'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/00c187e8-1820-4368-a393-d71dee7a8da3', 'https://app.thestorygraph.com/profile/00c187e8-1820-4368-a393-d71dee7a8da3', '00c187e8-1820-4368-a393-d71dee7a8da3'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/00ca5c3a-4c74-4a74-8542-82db320a0618', 'https://app.thestorygraph.com/profile/00ca5c3a-4c74-4a74-8542-82db320a0618', '00ca5c3a-4c74-4a74-8542-82db320a0618'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/0pen_b00ks', 'https://app.thestorygraph.com/profile/0pen_b00ks', '0pen_b00ks'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/0100', 'https://app.thestorygraph.com/profile/0100', '0100'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/008kore', 'https://app.thestorygraph.com/profile/008kore', '008kore'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/369', 'https://app.thestorygraph.com/profile/369', '369'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/_ce', 'https://app.thestorygraph.com/profile/_ce', '_ce'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/_ry', 'https://app.thestorygraph.com/profile/_ry', '_ry'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/m4r', 'https://app.thestorygraph.com/profile/m4r', 'm4r'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/mae', 'https://app.thestorygraph.com/profile/mae', 'mae'),  # wayback-200; live 200
    ('storygraph', 'https://app.thestorygraph.com/profile/0x76', 'https://app.thestorygraph.com/profile/0x76', '0x76'),  # wayback-200; live 200
    # RateYourMusic
    ('rateyourmusic', 'https://rateyourmusic.com/~003', 'https://rateyourmusic.com/~003', '003'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~0nlyLivingBoyinNY', 'https://rateyourmusic.com/~0nlyLivingBoyinNY', '0nlyLivingBoyinNY'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~1702_cl', 'https://rateyourmusic.com/~1702_cl', '1702_cl'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~1068396', 'https://rateyourmusic.com/~1068396', '1068396'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~000000marco', 'https://rateyourmusic.com/~000000marco', '000000marco'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~0Incarnadine0', 'https://rateyourmusic.com/~0Incarnadine0', '0Incarnadine0'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~0aa', 'https://rateyourmusic.com/~0aa', '0aa'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~2uh', 'https://rateyourmusic.com/~2uh', '2uh'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~367', 'https://rateyourmusic.com/~367', '367'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~_em', 'https://rateyourmusic.com/~_em', '_em'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~_oh', 'https://rateyourmusic.com/~_oh', '_oh'),  # wayback-200; live check blocked (403)
    ('rateyourmusic', 'https://rateyourmusic.com/~acd', 'https://rateyourmusic.com/~acd', 'acd'),  # wayback-200; live check blocked (403)
    # Flipboard
    ('flipboard', 'https://flipboard.com/@m', 'https://flipboard.com/@m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@saadaliraqi4oti', 'https://flipboard.com/@saadaliraqi4oti', 'saadaliraqi4oti'),  # wayback-200; live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@m0l0ch.rss', 'https://flipboard.com/@m0l0ch.rss', 'm0l0ch.rss'),  # wayback-200; live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@S_A_S', 'https://flipboard.com/@S_A_S', 'S_A_S'),  # wayback-200; live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@7awi_Layalina', 'https://flipboard.com/@7awi_Layalina', '7awi_Layalina'),  # wikidata:P9922 (Layalina); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@M0n1n1', 'https://flipboard.com/@M0n1n1', 'M0n1n1'),  # wayback-200; live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@ew', 'https://flipboard.com/@ew', 'ew'),  # wikidata:P9922 (Entertainment Weekly); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@Vox', 'https://flipboard.com/@Vox', 'Vox'),  # wikidata:P9922 (Vox); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@ign', 'https://flipboard.com/@ign', 'ign'),  # wikidata:P9922 (Q207708); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@WEF', 'https://flipboard.com/@WEF', 'WEF'),  # wikidata:P9922 (World Economic Forum); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@TPM', 'https://flipboard.com/@TPM', 'TPM'),  # wikidata:P9922 (Talking Points Memo); live 200 (unknown ids 404)
    ('flipboard', 'https://flipboard.com/@THR', 'https://flipboard.com/@THR', 'THR'),  # wikidata:P9922 (The Hollywood Reporter); live 200 (unknown ids 404)
    # Character.AI
    ('character_ai', 'https://character.ai/profile/--------8923920', 'https://character.ai/profile/--------8923920', '--------8923920'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/----', 'https://character.ai/profile/----', '----'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/----l____l', 'https://character.ai/profile/----l____l', '----l____l'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/-----CATNAP-----', 'https://character.ai/profile/-----CATNAP-----', '-----CATNAP-----'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/m1', 'https://character.ai/profile/m1', 'm1'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/M0T', 'https://character.ai/profile/M0T', 'M0T'),  # wayback-200; live 200
    ('character_ai', 'https://character.ai/profile/-', 'https://character.ai/profile/-', '-'),  # wayback-200; live 500
    ('character_ai', 'https://character.ai/profile/M.I.A', 'https://character.ai/profile/M.I.A', 'M.I.A'),  # wayback-200; live 500
    ('character_ai', 'https://character.ai/profile/M.M', 'https://character.ai/profile/M.M', 'M.M'),  # wayback-200; live 500
    ('character_ai', 'https://character.ai/profile/S.H', 'https://character.ai/profile/S.H', 'S.H'),  # wayback-200; live 500
    ('character_ai', 'https://character.ai/profile/K.D', 'https://character.ai/profile/K.D', 'K.D'),  # wayback-200; live 500
    ('character_ai', 'https://character.ai/profile/K.O', 'https://character.ai/profile/K.O', 'K.O'),  # wayback-200; live 500
    # Ollama
    ('ollama', 'https://ollama.com/m', 'https://ollama.com/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/sadiq-bd', 'https://ollama.com/sadiq-bd', 'sadiq-bd'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/s_emanuilov', 'https://ollama.com/s_emanuilov', 's_emanuilov'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/MadMind', 'https://ollama.com/MadMind', 'MadMind'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/sam860', 'https://ollama.com/sam860', 'sam860'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/kaelri', 'https://ollama.com/kaelri', 'kaelri'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/Keyvan', 'https://ollama.com/Keyvan', 'Keyvan'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/macadeliccc', 'https://ollama.com/macadeliccc', 'macadeliccc'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/sachasayan', 'https://ollama.com/sachasayan', 'sachasayan'),  # wayback-200; live 200 (unknown ids 404)
    ('ollama', 'https://ollama.com/kamekichi128', 'https://ollama.com/kamekichi128', 'kamekichi128'),  # wayback-200; live 200 (unknown ids 404)
    # Depop
    ('depop', 'http://www.depop.com/m2x/', 'https://www.depop.com/m2x', 'm2x'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/m00nlight_jewellery/', 'https://www.depop.com/m00nlight_jewellery', 'm00nlight_jewellery'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/m1lf_k4y/', 'https://www.depop.com/m1lf_k4y', 'm1lf_k4y'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/m3d/?brandIds=9&productId=445659642', 'https://www.depop.com/m3d', 'm3d'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/k9t/', 'https://www.depop.com/k9t', 'k9t'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/m1bm/', 'https://www.depop.com/m1bm', 'm1bm'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/m767/', 'https://www.depop.com/m767', 'm767'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/ma42/', 'https://www.depop.com/ma42', 'ma42'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/s3x0/', 'https://www.depop.com/s3x0', 's3x0'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/s6h6/', 'https://www.depop.com/s6h6', 's6h6'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/s8j7/', 'https://www.depop.com/s8j7', 's8j7'),  # wayback-200; live check blocked (403)
    ('depop', 'https://www.depop.com/sabi/', 'https://www.depop.com/sabi', 'sabi'),  # wayback-200; live check blocked (403)
    # Launchpad
    ('launchpad', 'https://launchpad.net/~0ol', 'https://launchpad.net/~0ol', '0ol'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~0.5a', 'https://launchpad.net/~0.5a', '0.5a'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~0-admin-mar-lt', 'https://launchpad.net/~0-admin-mar-lt', '0-admin-mar-lt'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~000852', 'https://launchpad.net/~000852', '000852'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~0-admin-n', 'https://launchpad.net/~0-admin-n', '0-admin-n'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~k', 'https://launchpad.net/~k', 'k'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~m-0', 'https://launchpad.net/~m-0', 'm-0'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~s-h', 'https://launchpad.net/~s-h', 's-h'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~k-9', 'https://launchpad.net/~k-9', 'k-9'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~k-d', 'https://launchpad.net/~k-d', 'k-d'),  # wayback-200; live 200 (unknown ids 404)
    ('launchpad', 'https://launchpad.net/~k-m', 'https://launchpad.net/~k-m', 'k-m'),  # wayback-200; live 200 (unknown ids 404)
    # CodeSandbox
    ('codesandbox', 'https://codesandbox.io/u/2rv', 'https://codesandbox.io/u/2rv', '2rv'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/_111oscar_manny', 'https://codesandbox.io/u/_111oscar_manny', '_111oscar_manny'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/a.fiodorov', 'https://codesandbox.io/u/a.fiodorov', 'a.fiodorov'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/7-game', 'https://codesandbox.io/u/7-game', '7-game'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/_50rb3t', 'https://codesandbox.io/u/_50rb3t', '_50rb3t'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/1076462153', 'https://codesandbox.io/u/1076462153', '1076462153'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/0mao0', 'https://codesandbox.io/u/0mao0', '0mao0'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/2Up1Down', 'https://codesandbox.io/u/2Up1Down', '2Up1Down'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/akx', 'https://codesandbox.io/u/akx', 'akx'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/kjk', 'https://codesandbox.io/u/kjk', 'kjk'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/kof', 'https://codesandbox.io/u/kof', 'kof'),  # wayback-200; live check blocked (403)
    ('codesandbox', 'https://codesandbox.io/u/kud', 'https://codesandbox.io/u/kud', 'kud'),  # wayback-200; live check blocked (403)
    # Juejin
    ('juejin', 'https://juejin.cn/user/1000968075623706', 'https://juejin.cn/user/1000968075623706', '1000968075623706'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1000974200084067', 'https://juejin.cn/user/1000974200084067', '1000974200084067'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002343353039517', 'https://juejin.cn/user/1002343353039517', '1002343353039517'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002353344124557', 'https://juejin.cn/user/1002353344124557', '1002353344124557'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002355477475799', 'https://juejin.cn/user/1002355477475799', '1002355477475799'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002355686907069', 'https://juejin.cn/user/1002355686907069', '1002355686907069'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002355886133575', 'https://juejin.cn/user/1002355886133575', '1002355886133575'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002358563932263', 'https://juejin.cn/user/1002358563932263', '1002358563932263'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002359236601703', 'https://juejin.cn/user/1002359236601703', '1002359236601703'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002360414694471', 'https://juejin.cn/user/1002360414694471', '1002360414694471'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002361512021496', 'https://juejin.cn/user/1002361512021496', '1002361512021496'),  # wayback-200; live 200
    ('juejin', 'https://juejin.cn/user/1002367800577592', 'https://juejin.cn/user/1002367800577592', '1002367800577592'),  # wayback-200; live 200
    # CSDN
    ('csdn', 'https://blog.csdn.net/K', 'https://blog.csdn.net/K', 'K'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/S.F.', 'https://blog.csdn.net/S.F.', 'S.F.'),  # wayback-200; live check blocked (521)
    ('csdn', 'http://blog.csdn.net/m0085_cn/', 'https://blog.csdn.net/m0085_cn', 'm0085_cn'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/M0000131141C', 'https://blog.csdn.net/M0000131141C', 'M0000131141C'),  # wayback-200; live check failed
    ('csdn', 'https://blog.csdn.net/M00n_', 'https://blog.csdn.net/M00n_', 'M00n_'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/K0113', 'https://blog.csdn.net/K0113', 'K0113'),  # wayback-200; live check blocked (521)
    ('csdn', 'http://blog.csdn.net/k0402/', 'https://blog.csdn.net/k0402', 'k0402'),  # wayback-200; live check failed
    ('csdn', 'https://blog.csdn.net/k0512', 'https://blog.csdn.net/k0512', 'k0512'),  # wayback-200; live check failed
    ('csdn', 'https://blog.csdn.net/K0711', 'https://blog.csdn.net/K0711', 'K0711'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/k0768', 'https://blog.csdn.net/k0768', 'k0768'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/k0933', 'https://blog.csdn.net/k0933', 'k0933'),  # wayback-200; live check blocked (521)
    ('csdn', 'https://blog.csdn.net/k01698', 'https://blog.csdn.net/k01698', 'k01698'),  # wayback-200; live check blocked (521)
    # Weights & Biases
    ('wandb', 'https://wandb.ai/a', 'https://forge.coreweave.com/profile/a', 'a'),  # wayback-200; live 200
    ('wandb', 'https://forge.coreweave.com/profile/denprotechnologies2', 'https://forge.coreweave.com/profile/denprotechnologies2', 'denprotechnologies2'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/sa-bizzabo.min.js', 'https://forge.coreweave.com/profile/sa-bizzabo.min.js', 'sa-bizzabo.min.js'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/a-agarwal', 'https://forge.coreweave.com/profile/a-agarwal', 'a-agarwal'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/balaji_ai', 'https://forge.coreweave.com/profile/balaji_ai', 'balaji_ai'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/S', 'https://forge.coreweave.com/profile/S', 'S'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/g', 'https://forge.coreweave.com/profile/g', 'g'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/m', 'https://forge.coreweave.com/profile/m', 'm'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/p', 'https://forge.coreweave.com/profile/p', 'p'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/t', 'https://forge.coreweave.com/profile/t', 't'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/d1g', 'https://forge.coreweave.com/profile/d1g', 'd1g'),  # wayback-200; live 200
    ('wandb', 'https://wandb.ai/d90', 'https://forge.coreweave.com/profile/d90', 'd90'),  # wayback-200; live 200
    # Chub.ai
    ('chub_ai', 'https://chub.ai/users/A_P', 'https://chub.ai/users/A_P', 'A_P'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/01000110_01010101', 'https://chub.ai/users/01000110_01010101', '01000110_01010101'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/Aegis-plus', 'https://chub.ai/users/Aegis-plus', 'Aegis-plus'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/02LemonMan_Face24', 'https://chub.ai/users/02LemonMan_Face24', '02LemonMan_Face24'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/042069', 'https://chub.ai/users/042069', '042069'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/01blinde', 'https://chub.ai/users/01blinde', '01blinde'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/0Sora0', 'https://chub.ai/users/0Sora0', '0Sora0'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/0x12', 'https://chub.ai/users/0x12', '0x12'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/100K', 'https://chub.ai/users/100K', '100K'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/1302', 'https://chub.ai/users/1302', '1302'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/1427', 'https://chub.ai/users/1427', '1427'),  # wayback-200; live 200
    ('chub_ai', 'https://chub.ai/users/M.4r', 'https://chub.ai/users/M.4r', 'M.4r'),  # wayback-200; live 404
    # Coursera
    ('coursera', 'https://www.coursera.org/user/85dca6cc1c1ccacdb8d6cbc3853c8eff', 'https://www.coursera.org/user/85dca6cc1c1ccacdb8d6cbc3853c8eff', '85dca6cc1c1ccacdb8d6cbc3853c8eff'),  # web:plan.md evidence; live 200
    ('coursera', 'https://www.coursera.org/user/6e657b6ddc13f1b27d9a4a7d3dffcf60', 'https://www.coursera.org/user/6e657b6ddc13f1b27d9a4a7d3dffcf60', '6e657b6ddc13f1b27d9a4a7d3dffcf60'),  # web:public LinkedIn profile (Daniel Parrillo); live 200
    ('coursera', 'https://www.coursera.org/user/i/fe7e73fef0333f550378979caa1d3347', 'https://www.coursera.org/user/fe7e73fef0333f550378979caa1d3347', 'fe7e73fef0333f550378979caa1d3347'),  # web:webpolicy.org/2014/09/04 (Jonathan Mayer); live 200
    ('coursera', 'https://www.coursera.org/user/i/66b48af35b7a3e54fdf15aff3da8a918', 'https://www.coursera.org/user/66b48af35b7a3e54fdf15aff3da8a918', '66b48af35b7a3e54fdf15aff3da8a918'),  # web:github.com/mgrebenets/mgrebenets-profile README; live 200
    # Udemy
    ('udemy', 'https://www.udemy.com/user/m-a-wajid-mudassir/', 'https://www.udemy.com/user/m-a-wajid-mudassir', 'm-a-wajid-mudassir'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/m-a-hasan-2/', 'https://www.udemy.com/user/m-a-hasan-2', 'm-a-hasan-2'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/m_a_tech/', 'https://www.udemy.com/user/m_a_tech', 'm_a_tech'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/m2up/', 'https://www.udemy.com/user/m2up', 'm2up'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/ma18/', 'https://www.udemy.com/user/ma18', 'ma18'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/m-tow/', 'https://www.udemy.com/user/m-tow', 'm-tow'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/m-v-5/', 'https://www.udemy.com/user/m-v-5', 'm-v-5'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/s2s-2/', 'https://www.udemy.com/user/s2s-2', 's2s-2'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/k-fly/', 'https://www.udemy.com/user/k-fly', 'k-fly'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/k3rst/', 'https://www.udemy.com/user/k3rst', 'k3rst'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/ka-22/', 'https://www.udemy.com/user/ka-22', 'ka-22'),  # wayback-200; live check blocked (403)
    ('udemy', 'https://www.udemy.com/user/kad-y/', 'https://www.udemy.com/user/kad-y', 'kad-y'),  # wayback-200; live check blocked (403)
    # Khan Academy
    ('khan_academy', 'https://www.khanacademy.org/profile/seanwallawallaofficial', 'https://www.khanacademy.org/profile/seanwallawallaofficial', 'seanwallawallaofficial'),  # web:github seanpm2001/KhanAcademyData_u-Seanwallawallaofficial README; live 200
    ('khan_academy', 'https://www.khanacademy.org/profile/darrylyeo', 'https://www.khanacademy.org/profile/darrylyeo', 'darrylyeo'),  # web:github darrylyeo/khan-academy-computer-programming README; live 200
    ('khan_academy', 'https://www.khanacademy.org/profile/raphaelrk', 'https://www.khanacademy.org/profile/raphaelrk', 'raphaelrk'),  # web:github raphaelrk/KhanAcademy-sketches README; live 200
    ('khan_academy', 'https://www.khanacademy.org/profile/kingcodefish', 'https://www.khanacademy.org/profile/kingcodefish', 'kingcodefish'),  # web:github kingcodefish/khan-academy-projects README; live 200
    ('khan_academy', 'https://www.khanacademy.org/profile/kaid_553656479258879622339276', 'https://www.khanacademy.org/profile/kaid_553656479258879622339276', 'kaid_553656479258879622339276'),  # web:github README (repo search: khan academy projects); live 200
    ('khan_academy', 'https://www.khanacademy.org/profile/lam.michael', 'https://www.khanacademy.org/profile/lam.michael', 'lam.michael'),  # web:github README (repo search: khan academy projects); live 200
    # Codecademy
    ('codecademy', 'https://www.codecademy.com/profiles/1Cp', 'https://www.codecademy.com/profiles/1Cp', '1Cp'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/010011000101000000001101?_gl=1%2Ad2oeli%2A_ga%2AMTU4NjYwNjU5NS4xNjUwODQzMzMy%2A_ga_3LRZM6TM9L%2AMTY1NTE1NzE0Mi43Ny4xLjE2NTUxNTgwOTcuMjU.', 'https://www.codecademy.com/profiles/010011000101000000001101', '010011000101000000001101'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/M.Dev', 'https://www.codecademy.com/profiles/M.Dev', 'M.Dev'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/-_________-', 'https://www.codecademy.com/profiles/-_________-', '-_________-'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/0_Tic', 'https://www.codecademy.com/profiles/0_Tic', '0_Tic'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/3044028420', 'https://www.codecademy.com/profiles/3044028420', '3044028420'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/0-brandon', 'https://www.codecademy.com/profiles/0-brandon', '0-brandon'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/0xTomas', 'https://www.codecademy.com/profiles/0xTomas', '0xTomas'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/3yE', 'https://www.codecademy.com/profiles/3yE', '3yE'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/K3u', 'https://www.codecademy.com/profiles/K3u', 'K3u'),  # wayback-200; live 200
    ('codecademy', 'https://www.codecademy.com/profiles/k8Y', 'https://www.codecademy.com/profiles/k8Y', 'k8Y'),  # wayback-200; live 200
    ('codecademy', 'http://www.codecademy.com/profiles/salo', 'https://www.codecademy.com/profiles/salo', 'salo'),  # wayback-200; live 200
    # freeCodeCamp
    ('freecodecamp', 'https://forum.freecodecamp.org/u/001', 'https://forum.freecodecamp.org/u/001', '001'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/010.carlos.labrador', 'https://forum.freecodecamp.org/u/010.carlos.labrador', '010.carlos.labrador'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/00.01.100', 'https://forum.freecodecamp.org/u/00.01.100', '00.01.100'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/0-0-Zero', 'https://forum.freecodecamp.org/u/0-0-Zero', '0-0-Zero'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/001_dan', 'https://forum.freecodecamp.org/u/001_dan', '001_dan'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/0000', 'https://forum.freecodecamp.org/u/0000', '0000'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/0000beesee', 'https://forum.freecodecamp.org/u/0000beesee', '0000beesee'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/000EZE000', 'https://forum.freecodecamp.org/u/000EZE000', '000EZE000'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/002', 'https://forum.freecodecamp.org/u/002', '002'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/01U', 'https://forum.freecodecamp.org/u/01U', '01U'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/077', 'https://forum.freecodecamp.org/u/077', '077'),  # wayback-200; live 200 (unknown ids 404)
    ('freecodecamp', 'https://forum.freecodecamp.org/u/0he', 'https://forum.freecodecamp.org/u/0he', '0he'),  # wayback-200; live 200 (unknown ids 404)
    # Semantic Scholar
    ('semantic_scholar', 'https://www.semanticscholar.org/author/%C2%A7-J.-M.-Petit/92249642', 'https://www.semanticscholar.org/author/92249642', '92249642'),  # wayback-200; live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/13734', 'https://www.semanticscholar.org/author/13734', '13734'),  # wikidata:P4012 (Eliezer Edwards); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/65664', 'https://www.semanticscholar.org/author/65664', '65664'),  # wikidata:P4012 (Gavin Rodney McGibbon); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/6178032', 'https://www.semanticscholar.org/author/6178032', '6178032'),  # wikidata:P4012 (Barack Obama); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/7416136', 'https://www.semanticscholar.org/author/7416136', '7416136'),  # wikidata:P4012 (Chenhui Ji); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/2776030', 'https://www.semanticscholar.org/author/2776030', '2776030'),  # wikidata:P4012 (Oliver Bandmann); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/1722759', 'https://www.semanticscholar.org/author/1722759', '1722759'),  # wikidata:P4012 (Michael Kremer); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/2097930', 'https://www.semanticscholar.org/author/2097930', '2097930'),  # wikidata:P4012 (P Armitage); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/2332528', 'https://www.semanticscholar.org/author/2332528', '2332528'),  # wikidata:P4012 (P. Chen); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/2923624', 'https://www.semanticscholar.org/author/2923624', '2923624'),  # wikidata:P4012 (Mirko van der Baan); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/3723480', 'https://www.semanticscholar.org/author/3723480', '3723480'),  # wikidata:P4012 (M.J. Bang); live check blocked (202)
    ('semantic_scholar', 'https://www.semanticscholar.org/author/-/1690110', 'https://www.semanticscholar.org/author/1690110', '1690110'),  # wikidata:P4012 (Richard Souvenir); live check blocked (202)
    # OSF
    ('osf', 'https://osf.io/user/64735', 'https://osf.io/user/64735', '64735'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/248sd', 'https://osf.io/user/248sd', '248sd'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/24das', 'https://osf.io/user/24das', '24das'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/26hfu', 'https://osf.io/user/26hfu', '26hfu'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/26m4q', 'https://osf.io/user/26m4q', '26m4q'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/26tyq', 'https://osf.io/user/26tyq', '26tyq'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/279qb', 'https://osf.io/user/279qb', '279qb'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/29cr5', 'https://osf.io/user/29cr5', '29cr5'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/2aexf', 'https://osf.io/user/2aexf', '2aexf'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/2ahkq', 'https://osf.io/user/2ahkq', '2ahkq'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/2aqye', 'https://osf.io/user/2aqye', '2aqye'),  # wayback-200; live 200
    ('osf', 'https://osf.io/user/2awsz', 'https://osf.io/user/2awsz', '2awsz'),  # wayback-200; live 200
    # iNaturalist
    ('inaturalist', 'https://www.inaturalist.org/people/m_d', 'https://www.inaturalist.org/people/m_d', 'm_d'),  # wayback-200; live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/m-antoniainfante2007', 'https://www.inaturalist.org/people/m-antoniainfante2007', 'm-antoniainfante2007'),  # wayback-200; live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/m-amsinckia', 'https://www.inaturalist.org/people/m-amsinckia', 'm-amsinckia'),  # wayback-200; live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/m__agalie', 'https://www.inaturalist.org/people/m__agalie', 'm__agalie'),  # wayback-200; live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/9129444', 'https://www.inaturalist.org/people/9129444', '9129444'),  # wikidata:P12022 (Alec Gosewehr); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/1', 'https://www.inaturalist.org/people/1', '1'),  # wikidata:P12022 (Ken-ichi Ueda); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/418', 'https://www.inaturalist.org/people/418', '418'),  # wikidata:P12022 (Q15136093); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/7943', 'https://www.inaturalist.org/people/7943', '7943'),  # wikidata:P12022 (Vijay Barve); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/6321', 'https://www.inaturalist.org/people/6321', '6321'),  # wikidata:P12022 (Roderic D. M. Page); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/don_k', 'https://www.inaturalist.org/people/don_k', 'don_k'),  # wikidata:P12022 (Donovan Kirkwood); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/59175', 'https://www.inaturalist.org/people/59175', '59175'),  # wikidata:P12022 (Cara-Lisa Schloots); live check blocked (403)
    ('inaturalist', 'https://www.inaturalist.org/people/70859', 'https://www.inaturalist.org/people/70859', '70859'),  # wikidata:P12022 (Siobhan Leachman); live check blocked (403)
    # FACEIT
    ('faceit', 'https://www.faceit.com/en/players/M', 'https://www.faceit.com/en/players/M', 'M'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/m-A-A-d', 'https://www.faceit.com/en/players/m-A-A-d', 'm-A-A-d'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/m00n-_-', 'https://www.faceit.com/en/players/m00n-_-', 'm00n-_-'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/M-bepis', 'https://www.faceit.com/en/players/M-bepis', 'M-bepis'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/M0R', 'https://www.faceit.com/en/players/M0R', 'M0R'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/M17', 'https://www.faceit.com/en/players/M17', 'M17'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/m1f', 'https://www.faceit.com/en/players/m1f', 'm1f'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/m1N', 'https://www.faceit.com/en/players/m1N', 'm1N'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/M4r', 'https://www.faceit.com/en/players/M4r', 'M4r'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/s0m', 'https://www.faceit.com/en/players/s0m', 's0m'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/s0p', 'https://www.faceit.com/en/players/s0p', 's0p'),  # wayback-200; live check blocked (403)
    ('faceit', 'https://www.faceit.com/en/players/S1a', 'https://www.faceit.com/en/players/S1a', 'S1a'),  # wayback-200; live check blocked (403)
    # Game Jolt
    ('gamejolt', 'https://gamejolt.com/@-M-', 'https://gamejolt.com/@-M-', '-M-'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@--FlamingGames--', 'https://gamejolt.com/@--FlamingGames--', '--FlamingGames--'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@..', 'https://gamejolt.com/@..', '..'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@----Lola----', 'https://gamejolt.com/@----Lola----', '----Lola----'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@--_Niko_--', 'https://gamejolt.com/@--_Niko_--', '--_Niko_--'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@10100', 'https://gamejolt.com/@10100', '10100'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@000000000000000000Deleted', 'https://gamejolt.com/@000000000000000000Deleted', '000000000000000000Deleted'),  # wayback-200; live 200
    ('gamejolt', 'http://gamejolt.com/@----XBRO----', 'https://gamejolt.com/@----XBRO----', '----XBRO----'),  # wayback-200; live 200
    ('gamejolt', 'https://gamejolt.com/@Aski', 'https://gamejolt.com/@Aski', 'Aski'),  # wikidata:P13243 (askiisoft); live 200
    ('gamejolt', 'https://gamejolt.com/@Zephy0', 'https://gamejolt.com/@Zephy0', 'Zephy0'),  # wikidata:P13243 (Angela He); live 200
    ('gamejolt', 'https://gamejolt.com/@vrglab', 'https://gamejolt.com/@vrglab', 'vrglab'),  # wikidata:P13243 (Vrglab); live 200
    ('gamejolt', 'https://gamejolt.com/@AppSir', 'https://gamejolt.com/@AppSir', 'AppSir'),  # wikidata:P13243 (AppSir); live 200
    # start.gg
    ('start_gg', 'https://www.start.gg/user/000809f1', 'https://www.start.gg/user/000809f1', '000809f1'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/000ad40b', 'https://www.start.gg/user/000ad40b', '000ad40b'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/000adab7', 'https://www.start.gg/user/000adab7', '000adab7'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/000c678b', 'https://www.start.gg/user/000c678b', '000c678b'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/00106895', 'https://www.start.gg/user/00106895', '00106895'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/001710a4', 'https://www.start.gg/user/001710a4', '001710a4'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/0017ccb6', 'https://www.start.gg/user/0017ccb6', '0017ccb6'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/0017e72e', 'https://www.start.gg/user/0017e72e', '0017e72e'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/0018c5cc', 'https://www.start.gg/user/0018c5cc', '0018c5cc'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/001fc1de', 'https://www.start.gg/user/001fc1de', '001fc1de'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/00211784', 'https://www.start.gg/user/00211784', '00211784'),  # wayback-200; live 200 (unknown ids 404)
    ('start_gg', 'https://www.start.gg/user/0024ea03', 'https://www.start.gg/user/0024ea03', '0024ea03'),  # wayback-200; live 200 (unknown ids 404)
    # CurseForge
    ('curseforge', 'https://www.curseforge.com/members/k2k/projects', 'https://www.curseforge.com/members/k2k', 'k2k'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/000_shadowake_amp/projects', 'https://www.curseforge.com/members/000_shadowake_amp', '000_shadowake_amp'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/007_ente/projects', 'https://www.curseforge.com/members/007_ente', '007_ente'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/0000003333/projects', 'https://www.curseforge.com/members/0000003333', '0000003333'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/0002niardnek/projects', 'https://www.curseforge.com/members/0002niardnek', '0002niardnek'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/M4ethor', 'https://www.curseforge.com/members/M4ethor', 'M4ethor'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/0blu/projects', 'https://www.curseforge.com/members/0blu', '0blu'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/0kk0/projects', 'https://www.curseforge.com/members/0kk0', '0kk0'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/0orc/projects', 'https://www.curseforge.com/members/0orc', '0orc'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/m18x', 'https://www.curseforge.com/members/m18x', 'm18x'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/m644/projects', 'https://www.curseforge.com/members/m644', 'm644'),  # wayback-200; live check blocked (403)
    ('curseforge', 'https://www.curseforge.com/members/m8ya/projects', 'https://www.curseforge.com/members/m8ya', 'm8ya'),  # wayback-200; live check blocked (403)
    # XDA Forums
    ('xda', 'https://xdaforums.com/m/0-beat.12936182/', 'https://xdaforums.com/m/0-beat.12936182', '0-beat.12936182'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/0-0-0.5261387/', 'https://xdaforums.com/m/0-0-0.5261387', '0-0-0.5261387'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/0-0.12920243/', 'https://xdaforums.com/m/0-0.12920243', '0-0.12920243'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/007_beezy.13310210/', 'https://xdaforums.com/m/007_beezy.13310210', '007_beezy.13310210'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/0-0.2281583/', 'https://xdaforums.com/m/0-0.2281583', '0-0.2281583'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/1.4274183/', 'https://xdaforums.com/m/1.4274183', '1.4274183'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/s.8407458/', 'https://xdaforums.com/m/s.8407458', 's.8407458'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/0-k.817917/', 'https://xdaforums.com/m/0-k.817917', '0-k.817917'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/1.12902652/', 'https://xdaforums.com/m/1.12902652', '1.12902652'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/m.13260791/', 'https://xdaforums.com/m/m.13260791', 'm.13260791'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/s.13224685/', 'https://xdaforums.com/m/s.13224685', 's.13224685'),  # wayback-200; live check blocked (403)
    ('xda', 'https://xdaforums.com/m/s.13278617/', 'https://xdaforums.com/m/s.13278617', 's.13278617'),  # wayback-200; live check blocked (403)
    # CHZZK
    ('chzzk', 'https://chzzk.naver.com/00026f1888e2f24eb916a34e177576a9', 'https://chzzk.naver.com/00026f1888e2f24eb916a34e177576a9', '00026f1888e2f24eb916a34e177576a9'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/000408038eda5ff54260c2a3b4315e28', 'https://chzzk.naver.com/000408038eda5ff54260c2a3b4315e28', '000408038eda5ff54260c2a3b4315e28'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/b171ba23d17440cc50b9e19a247f7749', 'https://chzzk.naver.com/b171ba23d17440cc50b9e19a247f7749', 'b171ba23d17440cc50b9e19a247f7749'),  # wikidata:P14163 (BuzzBean); live 200
    ('chzzk', 'https://chzzk.naver.com/4d0b7d3f825ea982b95f0a5c2b4782d3', 'https://chzzk.naver.com/4d0b7d3f825ea982b95f0a5c2b4782d3', '4d0b7d3f825ea982b95f0a5c2b4782d3'),  # wikidata:P14163 (Lilka); live 200
    ('chzzk', 'https://chzzk.naver.com/6ab86891e07489743437594c6e4dbf3a', 'https://chzzk.naver.com/6ab86891e07489743437594c6e4dbf3a', '6ab86891e07489743437594c6e4dbf3a'),  # wikidata:P14163 (Reva); live 200
    ('chzzk', 'https://chzzk.naver.com/88899e9e0f295937447205941f5ef9b2', 'https://chzzk.naver.com/88899e9e0f295937447205941f5ef9b2', '88899e9e0f295937447205941f5ef9b2'),  # wikidata:P14163 (Enyeong); live 200
    ('chzzk', 'https://chzzk.naver.com/000851405d53fd71ccd326163a164d87', 'https://chzzk.naver.com/000851405d53fd71ccd326163a164d87', '000851405d53fd71ccd326163a164d87'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/0008cf3fdbb8ef0e838dee5deef1e8a9', 'https://chzzk.naver.com/0008cf3fdbb8ef0e838dee5deef1e8a9', '0008cf3fdbb8ef0e838dee5deef1e8a9'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/000ef5698e0d4d32b10d2f50a5b3a140', 'https://chzzk.naver.com/000ef5698e0d4d32b10d2f50a5b3a140', '000ef5698e0d4d32b10d2f50a5b3a140'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/0011a5897cac34b2fc679d6d029bbbe0', 'https://chzzk.naver.com/0011a5897cac34b2fc679d6d029bbbe0', '0011a5897cac34b2fc679d6d029bbbe0'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/0013d1b983cccc5e89704a6cf9ac2b8f', 'https://chzzk.naver.com/0013d1b983cccc5e89704a6cf9ac2b8f', '0013d1b983cccc5e89704a6cf9ac2b8f'),  # wayback-200; live 200
    ('chzzk', 'https://chzzk.naver.com/002436e055e6172acfe8005c04ff851d', 'https://chzzk.naver.com/002436e055e6172acfe8005c04ff851d', '002436e055e6172acfe8005c04ff851d'),  # wayback-200; live 200
    # Huya
    ('huya', 'http://www.huya.com/s', 'https://www.huya.com/s', 's'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/k/?', 'https://www.huya.com/k', 'k'),  # wayback-200; live 200
    ('huya', 'https://www.huya.com/k3cqc', 'https://www.huya.com/k3cqc', 'k3cqc'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/k6426', 'https://www.huya.com/k6426', 'k6426'),  # wayback-200; live 200
    ('huya', 'https://www.huya.com/k8jun', 'https://www.huya.com/k8jun', 'k8jun'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/k2live', 'https://www.huya.com/k2live', 'k2live'),  # wayback-200; live 200
    ('huya', 'https://www.huya.com/k1ngone', 'https://www.huya.com/k1ngone', 'k1ngone'),  # wayback-200; live 200
    ('huya', 'https://www.huya.com/k666946', 'https://www.huya.com/k666946', 'k666946'),  # wayback-200; live 200
    ('huya', 'https://www.huya.com/k1510963', 'https://www.huya.com/k1510963', 'k1510963'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/kabao666', 'https://www.huya.com/kabao666', 'kabao666'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/k9zillang', 'https://www.huya.com/k9zillang', 'k9zillang'),  # wayback-200; live 200
    ('huya', 'http://www.huya.com/k29bailian', 'https://www.huya.com/k29bailian', 'k29bailian'),  # wayback-200; live 200
    # Douyu
    ('douyu', 'http://www.douyu.com/m18', 'https://www.douyu.com/m18', 'm18'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/M1n', 'https://www.douyu.com/M1n', 'M1n'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/m2m', 'https://www.douyu.com/m2m', 'm2m'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/m3g', 'https://www.douyu.com/m3g', 'm3g'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/m777', 'https://www.douyu.com/m777', 'm777'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/M888', 'https://www.douyu.com/M888', 'M888'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/kage', 'https://www.douyu.com/kage', 'kage'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/kaji', 'https://www.douyu.com/kaji', 'kaji'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/s1114', 'https://www.douyu.com/s1114', 's1114'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/s1134', 'https://www.douyu.com/s1134', 's1134'),  # wayback-200; live 200 (unknown ids 404)
    ('douyu', 'http://www.douyu.com/kaiba', 'https://www.douyu.com/kaiba', 'kaiba'),  # wayback-200; live 200 (unknown ids 404)
    # Rutube
    ('rutube', 'https://rutube.ru/channel/12145/', 'https://rutube.ru/channel/12145', '12145'),  # wikidata:P10152 (Gazgolder); live 200
    ('rutube', 'https://rutube.ru/channel/12056/', 'https://rutube.ru/channel/12056', '12056'),  # wikidata:P10152 (Soyuzmultfilm); live 200
    ('rutube', 'https://rutube.ru/channel/12058/', 'https://rutube.ru/channel/12058', '12058'),  # wikidata:P10152 (Disney Channel); live 200
    ('rutube', 'https://rutube.ru/channel/12217/', 'https://rutube.ru/channel/12217', '12217'),  # wikidata:P10152 (Masha and the Bear); live 200
    ('rutube', 'https://rutube.ru/channel/26327/', 'https://rutube.ru/channel/26327', '26327'),  # wikidata:P10152 (Ekaterina Gordon); live 200
    ('rutube', 'https://rutube.ru/channel/80871/', 'https://rutube.ru/channel/80871', '80871'),  # wikidata:P10152 (Neuromir TV); live 200
    ('rutube', 'https://rutube.ru/channel/19898/', 'https://rutube.ru/channel/19898', '19898'),  # wikidata:P10152 (Lolita Milyavskaya); live 200
    ('rutube', 'https://rutube.ru/channel/00000000/', 'https://rutube.ru/channel/00000000', '00000000'),  # wayback-200; live 404
    ('rutube', 'https://rutube.ru/channel/4072/', 'https://rutube.ru/channel/4072', '4072'),  # wikidata:P10152 (Alexander Pushnoy); live 404
    ('rutube', 'https://rutube.ru/channel/2223/', 'https://rutube.ru/channel/2223', '2223'),  # wikidata:P10152 (Atomic Forest); live 404
    ('rutube', 'https://rutube.ru/channel/2450/', 'https://rutube.ru/channel/2450', '2450'),  # wikidata:P10152 (Bratya Safronovy); live 404
    ('rutube', 'https://rutube.ru/channel/11004/', 'https://rutube.ru/channel/11004', '11004'),  # wikidata:P10152 (Valery Fedorovich); live 404
    # SOOP (AfreecaTV)
    ('soop', 'https://www.sooplive.com/station/agf', 'https://www.sooplive.com/station/agf', 'agf'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/0136d146dc33ee6abc656509ba0c4a65', 'https://www.sooplive.com/station/0136d146dc33ee6abc656509ba0c4a65', '0136d146dc33ee6abc656509ba0c4a65'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/9m...', 'https://www.sooplive.com/station/9m...', '9m...'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/app-ads.txt', 'https://www.sooplive.com/station/app-ads.txt', 'app-ads.txt'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/000112', 'https://www.sooplive.com/station/000112', '000112'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/002oo1', 'https://www.sooplive.com/station/002oo1', '002oo1'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/asl', 'https://www.sooplive.com/station/asl', 'asl'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/atl', 'https://www.sooplive.com/station/atl', 'atl'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/kdl', 'https://www.sooplive.com/station/kdl', 'kdl'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/2kyo', 'https://www.sooplive.com/station/2kyo', '2kyo'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/afhs', 'https://www.sooplive.com/station/afhs', 'afhs'),  # wayback-200; live 200
    ('soop', 'https://www.sooplive.com/station/asdf', 'https://www.sooplive.com/station/asdf', 'asdf'),  # wayback-200; live 200
    # Nimo TV
    ('nimo_tv', 'https://www.nimo.tv/m', 'https://www.nimo.tv/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/madrugonexnimotv?_lang=1093', 'https://www.nimo.tv/madrugonexnimotv', 'madrugonexnimotv'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/MaguiSunshine', 'https://www.nimo.tv/MaguiSunshine', 'MaguiSunshine'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/m16', 'https://www.nimo.tv/m16', 'm16'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/k1ng', 'https://www.nimo.tv/k1ng', 'k1ng'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/kafa', 'https://www.nimo.tv/kafa', 'kafa'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/m16ff', 'https://www.nimo.tv/m16ff', 'm16ff'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/ma20k?_lang=1034', 'https://www.nimo.tv/ma20k', 'ma20k'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/madly', 'https://www.nimo.tv/madly', 'madly'),  # wayback-200; live 200 (unknown ids 404)
    ('nimo_tv', 'https://www.nimo.tv/mahdi', 'https://www.nimo.tv/mahdi', 'mahdi'),  # wayback-200; live 200 (unknown ids 404)
    # Audioboom
    ('audioboom', 'https://audioboom.com/channels/69993-sky-news-radio', 'https://audioboom.com/channels/69993', '69993'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/106016-planet-rock', 'https://audioboom.com/channels/106016', '106016'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/608902-bbc-radio-sheffield', 'https://audioboom.com/channels/608902', '608902'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/617528-bbc-three-counties-radio', 'https://audioboom.com/channels/617528', '617528'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/657989-blind-veterans-uk', 'https://audioboom.com/channels/657989', '657989'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/1050095-football-heaven', 'https://audioboom.com/channels/1050095', '1050095'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/1054469', 'https://audioboom.com/channels/1054469', '1054469'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/2003735-william-hill-snooker', 'https://audioboom.com/channels/2003735', '2003735'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/2011733-digital-music-trends', 'https://audioboom.com/channels/2011733', '2011733'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/2012387-star-fm-riverina', 'https://audioboom.com/channels/2012387', '2012387'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/2012417-star-fm', 'https://audioboom.com/channels/2012417', '2012417'),  # wayback-200; live 200 (unknown ids 404)
    ('audioboom', 'https://audioboom.com/channels/2035593-bournemouth-daily-echo', 'https://audioboom.com/channels/2035593', '2035593'),  # wayback-200; live 200 (unknown ids 404)
    # Jamendo
    ('jamendo', 'https://www.jamendo.com/user/0/_', 'https://www.jamendo.com/user/0', '0'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/maiacampbellsfu?language=en', 'https://www.jamendo.com/user/maiacampbellsfu', 'maiacampbellsfu'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/...Orlando...?language=en', 'https://www.jamendo.com/user/...Orlando...', '...Orlando...'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/mature-moms?language=en', 'https://www.jamendo.com/user/mature-moms', 'mature-moms'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/Meridia_online_buy_cheapest', 'https://www.jamendo.com/user/Meridia_online_buy_cheapest', 'Meridia_online_buy_cheapest'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/1003234/zaharov-valery', 'https://www.jamendo.com/user/1003234', '1003234'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/...Orlando?language=en', 'https://www.jamendo.com/user/...Orlando', '...Orlando'),  # wayback-200; live 200
    ('jamendo', 'http://www.jamendo.com/user/5', 'https://www.jamendo.com/user/5', '5'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/MD5?language=en', 'https://www.jamendo.com/user/MD5', 'MD5'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/sam', 'https://www.jamendo.com/user/sam', 'sam'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/KIM?language=en', 'https://www.jamendo.com/user/KIM', 'KIM'),  # wayback-200; live 200
    ('jamendo', 'https://www.jamendo.com/user/5347/holygreg', 'https://www.jamendo.com/user/5347', '5347'),  # wayback-200; live 200
    # Bio.link
    ('bio_link', 'https://bio.link/m1m', 'https://bio.link/m1m', 'm1m'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/m14_3y3', 'https://bio.link/m14_3y3', 'm14_3y3'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/M5ctX', 'https://bio.link/M5ctX', 'M5ctX'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/m4i', 'https://bio.link/m4i', 'm4i'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/m_m', 'https://bio.link/m_m', 'm_m'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/s_p', 'https://bio.link/s_p', 's_p'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/Kai', 'https://bio.link/Kai', 'Kai'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/m1ka', 'https://bio.link/m1ka', 'm1ka'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/m717', 'https://bio.link/m717', 'm717'),  # wayback-200; live 200 (unknown ids 404)
    ('bio_link', 'https://bio.link/maas', 'https://bio.link/maas', 'maas'),  # wayback-200; live 200 (unknown ids 404)
    # Taplink
    ('taplink', 'https://taplink.cc/m._robiu_atoillah', 'https://taplink.cc/m._robiu_atoillah', 'm._robiu_atoillah'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.0088.kz', 'https://taplink.cc/m.0088.kz', 'm.0088.kz'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.3011_', 'https://taplink.cc/m.3011_', 'm.3011_'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.a', 'https://taplink.cc/m.a', 'm.a'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.a.d', 'https://taplink.cc/m.a.d', 'm.a.d'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.a.g', 'https://taplink.cc/m.a.g', 'm.a.g'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.ale', 'https://taplink.cc/m.ale', 'm.ale'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.ali', 'https://taplink.cc/m.ali', 'm.ali'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m.ars', 'https://taplink.cc/m.ars', 'm.ars'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/s.ayy', 'https://taplink.cc/s.ayy', 's.ayy'),  # wayback-200; live 200
    ('taplink', 'https://taplink.cc/m', 'https://taplink.cc/m', 'm'),  # wayback-200; live 301
    ('taplink', 'https://taplink.cc/s', 'https://taplink.cc/s', 's'),  # wayback-200; live 301
    # solo.to
    ('solo_to', 'https://solo.to/m.drippy', 'https://solo.to/m.drippy', 'm.drippy'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/m-nivn', 'https://solo.to/m-nivn', 'm-nivn'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/m.s_1', 'https://solo.to/m.s_1', 'm.s_1'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/K', 'https://solo.to/K', 'K'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/ma', 'https://solo.to/ma', 'ma'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/k2', 'https://solo.to/k2', 'k2'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/k_', 'https://solo.to/k_', 'k_'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/m10', 'https://solo.to/m10', 'm10'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/m11', 'https://solo.to/m11', 'm11'),  # wayback-200; live 200 (unknown ids 404)
    ('solo_to', 'https://solo.to/m1i', 'https://solo.to/m1i', 'm1i'),  # wayback-200; live 200 (unknown ids 404)
    # Hoo.be
    ('hoo_be', 'https://hoo.be/m4r', 'https://hoo.be/m4r', 'm4r'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/mackenziemariesmith', 'https://hoo.be/mackenziemariesmith', 'mackenziemariesmith'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/m.sfpp', 'https://hoo.be/m.sfpp', 'm.sfpp'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/m2_qbacademy', 'https://hoo.be/m2_qbacademy', 'm2_qbacademy'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/SageSpot', 'https://hoo.be/SageSpot', 'SageSpot'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/sac', 'https://hoo.be/sac', 'sac'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/sam', 'https://hoo.be/sam', 'sam'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'http://hoo.be/mack', 'https://hoo.be/mack', 'mack'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/mads', 'https://hoo.be/mads', 'mads'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/maes', 'https://hoo.be/maes', 'maes'),  # wayback-200; live 200 (unknown ids 404)
    ('hoo_be', 'https://hoo.be/s4rp', 'https://hoo.be/s4rp', 's4rp'),  # wayback-200; live 200 (unknown ids 404)
    # Throne
    ('throne', 'https://throne.com/m', 'https://throne.com/m', 'm'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m.miccostumes.com', 'https://throne.com/m.miccostumes.com', 'm.miccostumes.com'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m.b.jossi', 'https://throne.com/m.b.jossi', 'm.b.jossi'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m-35', 'https://throne.com/m-35', 'm-35'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m00_n13', 'https://throne.com/m00_n13', 'm00_n13'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/M0NTER0', 'https://throne.com/M0NTER0', 'M0NTER0'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/S', 'https://throne.com/S', 'S'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m-g', 'https://throne.com/m-g', 'm-g'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m01', 'https://throne.com/m01', 'm01'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m09', 'https://throne.com/m09', 'm09'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m0e', 'https://throne.com/m0e', 'm0e'),  # wayback-200; live check blocked (429)
    ('throne', 'https://throne.com/m0m', 'https://throne.com/m0m', 'm0m'),  # wayback-200; live check blocked (429)
    # Fanfix
    ('fanfix', 'https://app.fanfix.io/@.spicyfeet', 'https://app.fanfix.io/@.spicyfeet', '.spicyfeet'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@adam-545d9c', 'https://app.fanfix.io/@adam-545d9c', 'adam-545d9c'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@1kyle8', 'https://app.fanfix.io/@1kyle8', '1kyle8'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@cxtt', 'https://app.fanfix.io/@cxtt', 'cxtt'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@5ddie', 'https://app.fanfix.io/@5ddie', '5ddie'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@4aodalys', 'https://app.fanfix.io/@4aodalys', '4aodalys'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@acehimiko', 'https://app.fanfix.io/@acehimiko', 'acehimiko'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@alee_babe', 'https://app.fanfix.io/@alee_babe', 'alee_babe'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@alisssaoddo', 'https://app.fanfix.io/@alisssaoddo', 'alisssaoddo'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@bails', 'https://app.fanfix.io/@bails', 'bails'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@belsfaith', 'https://app.fanfix.io/@belsfaith', 'belsfaith'),  # wayback-200; live 200 (unknown ids 404)
    ('fanfix', 'https://app.fanfix.io/@brynhildurgunnlaugs', 'https://app.fanfix.io/@brynhildurgunnlaugs', 'brynhildurgunnlaugs'),  # wayback-200; live 200 (unknown ids 404)
    # Campsite.bio
    ('campsite_bio', 'https://campsite.bio/kak', 'https://campsite.bio/kak', 'kak'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/m88directthethao', 'https://campsite.bio/m88directthethao', 'm88directthethao'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/m.baec', 'https://campsite.bio/m.baec', 'm.baec'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/magenta_atnegam', 'https://campsite.bio/magenta_atnegam', 'magenta_atnegam'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/macd', 'https://campsite.bio/macd', 'macd'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/s4am', 'https://campsite.bio/s4am', 's4am'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/sacm/', 'https://campsite.bio/sacm', 'sacm'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/sakr', 'https://campsite.bio/sakr', 'sakr'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/kaed', 'https://campsite.bio/kaed', 'kaed'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/kage', 'https://campsite.bio/kage', 'kage'),  # wayback-200; live 200 (unknown ids 404)
    ('campsite_bio', 'https://campsite.bio/kali', 'https://campsite.bio/kali', 'kali'),  # wayback-200; live 200 (unknown ids 404)
    # 500px
    ('500px', 'https://500px.com/p/m-m?', 'https://500px.com/p/m-m', 'm-m'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m-bychkova452649039', 'https://500px.com/p/m-bychkova452649039', 'm-bychkova452649039'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m-9712824', 'https://500px.com/p/m-9712824', 'm-9712824'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m07amed_hussein?', 'https://500px.com/p/m07amed_hussein', 'm07amed_hussein'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/K1selev', 'https://500px.com/p/K1selev', 'K1selev'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/s29', 'https://500px.com/p/s29', 's29'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m-kh?', 'https://500px.com/p/m-kh', 'm-kh'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m12n?', 'https://500px.com/p/m12n', 'm12n'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m1nd?', 'https://500px.com/p/m1nd', 'm1nd'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m6w6?', 'https://500px.com/p/m6w6', 'm6w6'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/m7r3?', 'https://500px.com/p/m7r3', 'm7r3'),  # wayback-200; live 200
    ('500px', 'https://500px.com/p/s-we', 'https://500px.com/p/s-we', 's-we'),  # wayback-200; live 200
    # Redbubble
    ('redbubble', 'https://www.redbubble.com/people/M-A-Calligraphy/shop', 'https://www.redbubble.com/people/M-A-Calligraphy', 'M-A-Calligraphy'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'https://www.redbubble.com/people/M-2-B/explore?asc=u&page=1&sortOrder=recent', 'https://www.redbubble.com/people/M-2-B', 'M-2-B'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/k-dh?', 'https://www.redbubble.com/people/k-dh', 'k-dh'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/m-a-k', 'https://www.redbubble.com/people/m-a-k', 'm-a-k'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'https://www.redbubble.com/people/m-ace/shop', 'https://www.redbubble.com/people/m-ace', 'm-ace'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'https://www.redbubble.com/people/m-ale/shop', 'https://www.redbubble.com/people/m-ale', 'm-ale'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'https://www.redbubble.com/people/k-afw/shop', 'https://www.redbubble.com/people/k-afw', 'k-afw'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/k-gen', 'https://www.redbubble.com/people/k-gen', 'k-gen'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/---andy---', 'https://www.redbubble.com/people/---andy---', '---andy---'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'https://www.redbubble.com/people/---clara---/shop', 'https://www.redbubble.com/people/---clara---', '---clara---'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/---o-g-m---', 'https://www.redbubble.com/people/---o-g-m---', '---o-g-m---'),  # wayback-200; live 200 (unknown ids 404)
    ('redbubble', 'http://www.redbubble.com/people/--amigo--', 'https://www.redbubble.com/people/--amigo--', '--amigo--'),  # wayback-200; live 200 (unknown ids 404)
    # Cara
    ('cara', 'https://cara.app/-c0sm0thegaypastry-', 'https://cara.app/-c0sm0thegaypastry-', '-c0sm0thegaypastry-'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/-joe-', 'https://cara.app/-joe-', '-joe-'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/0000', 'https://cara.app/0000', '0000'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/00-marumaru', 'https://cara.app/00-marumaru', '00-marumaru'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/017s', 'https://cara.app/017s', '017s'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/01nu', 'https://cara.app/01nu', '01nu'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/11en', 'https://cara.app/11en', '11en'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/1310', 'https://cara.app/1310', '1310'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/1717', 'https://cara.app/1717', '1717'),  # wayback-200; live 200 (unknown ids 404)
    ('cara', 'https://cara.app/1912', 'https://cara.app/1912', '1912'),  # wayback-200; live 200 (unknown ids 404)
    # Sketchfab
    ('sketchfab', 'https://sketchfab.com/S-A', 'https://sketchfab.com/S-A', 'S-A'),  # wayback-200; live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/m-11356016moe-dl.edu.my', 'https://sketchfab.com/m-11356016moe-dl.edu.my', 'm-11356016moe-dl.edu.my'),  # wayback-200; live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/M-A.L', 'https://sketchfab.com/M-A.L', 'M-A.L'),  # wayback-200; live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/m-13126533', 'https://sketchfab.com/m-13126533', 'm-13126533'),  # wayback-200; live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/m.l_3.69_design', 'https://sketchfab.com/m.l_3.69_design', 'm.l_3.69_design'),  # wayback-200; live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/JoshUniverse', 'https://sketchfab.com/JoshUniverse', 'JoshUniverse'),  # wikidata:P14099 (Josh Universe); live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/NentheadMines', 'https://sketchfab.com/NentheadMines', 'NentheadMines'),  # wikidata:P14099 (Nenthead Mines); live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/mohamedfawzyps', 'https://sketchfab.com/mohamedfawzyps', 'mohamedfawzyps'),  # wikidata:P14099 (Mohamed Fawzy); live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/designstudiopro', 'https://sketchfab.com/designstudiopro', 'designstudiopro'),  # wikidata:P14099 (Design Studio Pro); live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/alexandre.maignan', 'https://sketchfab.com/alexandre.maignan', 'alexandre.maignan'),  # wikidata:P14099 (Alexandre Maignan); live 200 (unknown ids 404)
    ('sketchfab', 'https://sketchfab.com/GermanMaritimeMuseum', 'https://sketchfab.com/GermanMaritimeMuseum', 'GermanMaritimeMuseum'),  # wikidata:P14099 (German Maritime Museum); live 200 (unknown ids 404)
    # Thingiverse
    ('thingiverse', 'https://www.thingiverse.com/m-j/designs', 'https://www.thingiverse.com/m-j', 'm-j'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/s0lve-et-c0agula/designs', 'https://www.thingiverse.com/s0lve-et-c0agula', 's0lve-et-c0agula'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/m-arti/designs', 'https://www.thingiverse.com/m-arti', 'm-arti'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/s0ciabl3ng_tg/designs', 'https://www.thingiverse.com/s0ciabl3ng_tg', 's0ciabl3ng_tg'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/M-Industries/designs', 'https://www.thingiverse.com/M-Industries', 'M-Industries'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/m/designs', 'https://www.thingiverse.com/m', 'm'),  # wayback-200; live 200
    ('thingiverse', 'http://www.thingiverse.com/m0a/designs', 'https://www.thingiverse.com/m0a', 'm0a'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/s-k/designs', 'https://www.thingiverse.com/s-k', 's-k'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/m013/designs', 'https://www.thingiverse.com/m013', 'm013'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/M06Z/designs', 'https://www.thingiverse.com/M06Z', 'M06Z'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/s0ma/designs', 'https://www.thingiverse.com/s0ma', 's0ma'),  # wayback-200; live 200
    ('thingiverse', 'https://www.thingiverse.com/s199/designs', 'https://www.thingiverse.com/s199', 's199'),  # wayback-200; live 200
    # Fur Affinity
    ('furaffinity', 'https://www.furaffinity.net/user/m/', 'https://www.furaffinity.net/user/m', 'm'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/m-severova644753596', 'https://www.furaffinity.net/user/m-severova644753596', 'm-severova644753596'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'http://www.furaffinity.net/user/m-0-ths', 'https://www.furaffinity.net/user/m-0-ths', 'm-0-ths'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/s/', 'https://www.furaffinity.net/user/s', 's'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/k/', 'https://www.furaffinity.net/user/k', 'k'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'http://www.furaffinity.net/user/m-k/', 'https://www.furaffinity.net/user/m-k', 'm-k'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/m-m/', 'https://www.furaffinity.net/user/m-m', 'm-m'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/m-o/', 'https://www.furaffinity.net/user/m-o', 'm-o'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/s-7/', 'https://www.furaffinity.net/user/s-7', 's-7'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/s-j/', 'https://www.furaffinity.net/user/s-j', 's-j'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'https://www.furaffinity.net/user/k-5/', 'https://www.furaffinity.net/user/k-5', 'k-5'),  # wayback-200; live check blocked (403)
    ('furaffinity', 'http://www.furaffinity.net/user/k-9/', 'https://www.furaffinity.net/user/k-9', 'k-9'),  # wayback-200; live check blocked (403)
    # Toyhouse
    ('toyhouse', 'https://toyhou.se/plyashka_fragolino', 'https://toyhou.se/plyashka_fragolino', 'plyashka_fragolino'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/D0NQU1X0T3_', 'https://toyhou.se/D0NQU1X0T3_', 'D0NQU1X0T3_'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/IttsPidge', 'https://toyhou.se/IttsPidge', 'IttsPidge'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/atxar', 'https://toyhou.se/atxar', 'atxar'),  # web:websearch (commissions post); live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/Suroi', 'https://toyhou.se/Suroi', 'Suroi'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/susie', 'https://toyhou.se/susie', 'susie'),  # web:websearch: toyhou.se/susie; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/reormy', 'https://toyhou.se/reormy', 'reormy'),  # web:websearch: toyhou.se/reormy; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/Xyonnex', 'https://toyhou.se/Xyonnex', 'Xyonnex'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/uncorpus', 'https://toyhou.se/uncorpus', 'uncorpus'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/Seapupper', 'https://toyhou.se/Seapupper', 'Seapupper'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/Sproutbird', 'https://toyhou.se/Sproutbird', 'Sproutbird'),  # web:websearch; live 200 (unknown ids 404)
    ('toyhouse', 'https://toyhou.se/CoyoteeCove', 'https://toyhou.se/CoyoteeCove', 'CoyoteeCove'),  # web:websearch; live 200 (unknown ids 404)
    # Are.na
    ('are_na', 'https://www.are.na/m-e', 'https://www.are.na/m-e', 'm-e'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-a-arw9dered9g', 'https://www.are.na/m-a-arw9dered9g', 'm-a-arw9dered9g'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-8dtyx-su_6q', 'https://www.are.na/m-8dtyx-su_6q', 'm-8dtyx-su_6q'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/s', 'https://www.are.na/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/k-c', 'https://www.are.na/k-c', 'k-c'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-ad', 'https://www.are.na/m-ad', 'm-ad'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/s-hu', 'https://www.are.na/s-hu', 's-hu'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/k-bob', 'https://www.are.na/k-bob', 'k-bob'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/k-g-t', 'https://www.are.na/k-g-t', 'k-g-t'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-alvarado-7h2blshhzzy', 'https://www.are.na/m-alvarado-7h2blshhzzy', 'm-alvarado-7h2blshhzzy'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-bauer', 'https://www.are.na/m-bauer', 'm-bauer'),  # wayback-200; live 200 (unknown ids 404)
    ('are_na', 'https://www.are.na/m-c-1503650437', 'https://www.are.na/m-c-1503650437', 'm-c-1503650437'),  # wayback-200; live 200 (unknown ids 404)
    # Buttondown
    ('buttondown', 'https://buttondown.com/099', 'https://buttondown.com/099', '099'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/1001smartcities', 'https://buttondown.com/1001smartcities', '1001smartcities'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/samantha-andrews', 'https://buttondown.com/samantha-andrews', 'samantha-andrews'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/kaiso_one', 'https://buttondown.com/kaiso_one', 'kaiso_one'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/0xadada', 'https://buttondown.com/0xadada', '0xadada'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/MaddieTenKnives', 'https://buttondown.com/MaddieTenKnives', 'MaddieTenKnives'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/s/', 'https://buttondown.com/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/11ty', 'https://buttondown.com/11ty', '11ty'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/mag7', 'https://buttondown.com/mag7', 'mag7'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/sade', 'https://buttondown.com/sade', 'sade'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/SAIL', 'https://buttondown.com/SAIL', 'SAIL'),  # wayback-200; live 200 (unknown ids 404)
    ('buttondown', 'https://buttondown.com/s3thi/', 'https://buttondown.com/s3thi', 's3thi'),  # wayback-200; live 200 (unknown ids 404)
    # Paragraph
    ('paragraph', 'https://paragraph.com/@%D0%B0%D1%80%D1%80%D3%8F%D0%B5', 'https://paragraph.com/@%D0%B0%D1%80%D1%80%D3%8F%D0%B5', '%D0%B0%D1%80%D1%80%D3%8F%D0%B5'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@%E5%8D%A2%E6%9C%AC%E4%BC%9F', 'https://paragraph.com/@%E5%8D%A2%E6%9C%AC%E4%BC%9F', '%E5%8D%A2%E6%9C%AC%E4%BC%9F'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@s-navaneeth-krishna-talks-r-n-b', 'https://paragraph.com/@s-navaneeth-krishna-talks-r-n-b', 's-navaneeth-krishna-talks-r-n-b'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9.%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9', 'https://paragraph.com/@%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9.%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9', '%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9.%E3%82%AB%E3%83%A9%E3%82%AB%E3%83%A9'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@m-11', 'https://paragraph.com/@m-11', 'm-11'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@%DB%B5%DB%B5%DB%B2%DB%B8', 'https://paragraph.com/@%DB%B5%DB%B5%DB%B2%DB%B8', '%DB%B5%DB%B5%DB%B2%DB%B8'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@m-2', 'https://paragraph.com/@m-2', 'm-2'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@m-4', 'https://paragraph.com/@m-4', 'm-4'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@m10', 'https://paragraph.com/@m10', 'm10'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@k-3', 'https://paragraph.com/@k-3', 'k-3'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@k-6', 'https://paragraph.com/@k-6', 'k-6'),  # wayback-200; live 200 (unknown ids 404)
    ('paragraph', 'https://paragraph.com/@m-13', 'https://paragraph.com/@m-13', 'm-13'),  # wayback-200; live 200 (unknown ids 404)
    # Royal Road
    ('royal_road', 'https://www.royalroad.com/profile/1', 'https://www.royalroad.com/profile/1', '1'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10', 'https://www.royalroad.com/profile/10', '10'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/100', 'https://www.royalroad.com/profile/100', '100'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/1000', 'https://www.royalroad.com/profile/1000', '1000'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10000', 'https://www.royalroad.com/profile/10000', '10000'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10001', 'https://www.royalroad.com/profile/10001', '10001'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10002', 'https://www.royalroad.com/profile/10002', '10002'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10003', 'https://www.royalroad.com/profile/10003', '10003'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10004', 'https://www.royalroad.com/profile/10004', '10004'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/10005', 'https://www.royalroad.com/profile/10005', '10005'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/100000', 'https://www.royalroad.com/profile/100000', '100000'),  # wayback-200; live check blocked (403)
    ('royal_road', 'https://www.royalroad.com/profile/100001', 'https://www.royalroad.com/profile/100001', '100001'),  # wayback-200; live check blocked (403)
    # Scribd
    ('scribd', 'https://www.scribd.com/user/1000000185/srinikeshkottala-25', 'https://www.scribd.com/user/1000000185/srinikeshkottala-25', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/100000030/Amit-Gupta', 'https://www.scribd.com/user/100000030/Amit-Gupta', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/1000000/koga17', 'https://www.scribd.com/user/1000000/koga17', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/100000057/Yogesh-Dixit', 'https://www.scribd.com/user/100000057/Yogesh-Dixit', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/30/CAP', 'https://www.scribd.com/user/30/CAP', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/500002401/r', 'https://www.scribd.com/user/500002401/r', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/9000041/sanu', 'https://www.scribd.com/user/9000041/sanu', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/300000623/Eva', 'https://www.scribd.com/user/300000623/Eva', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/300001707/Jim', 'https://www.scribd.com/user/300001707/Jim', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/400001057/umi', 'https://www.scribd.com/user/400001057/umi', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/500001024/jay', 'https://www.scribd.com/user/500001024/jay', None),  # wayback-200; live 200
    ('scribd', 'https://www.scribd.com/user/500001332/S-M', 'https://www.scribd.com/user/500001332/S-M', None),  # wayback-200; live 200
    # Issuu
    ('issuu', 'https://issuu.com/m-2c', 'https://issuu.com/m-2c', 'm-2c'),  # wayback-200; live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/AustralianNursingFederation', 'https://issuu.com/AustralianNursingFederation', 'AustralianNursingFederation'),  # wikidata:P9921 (Australian Nursing & Midwifery Journal); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/rbia', 'https://issuu.com/rbia', 'rbia'),  # wikidata:P9921 (Cirrus Media); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/bdlf', 'https://issuu.com/bdlf', 'bdlf'),  # wikidata:P9921 (Database of Photography Books); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/dosb', 'https://issuu.com/dosb', 'dosb'),  # wikidata:P9921 (German Olympic Sports Confederation); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/duic', 'https://issuu.com/duic', 'duic'),  # wikidata:P9921 (DUIC); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/bienal', 'https://issuu.com/bienal', 'bienal'),  # wikidata:P9921 (São Paulo Art Biennial); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/aauschooloffashion', 'https://issuu.com/aauschooloffashion', 'aauschooloffashion'),  # wikidata:P9921 (Academy of Art University School of Fashion); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/pnwmarketplace', 'https://issuu.com/pnwmarketplace', 'pnwmarketplace'),  # wikidata:P9921 (Sound Publishing); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/theplazadoha', 'https://issuu.com/theplazadoha', 'theplazadoha'),  # wikidata:P9921 (The Plaza Doha, LXR Hotels & Resorts); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/taxmann9', 'https://issuu.com/taxmann9', 'taxmann9'),  # wikidata:P9921 (Taxmann); live 200 (unknown ids 404)
    ('issuu', 'https://issuu.com/hgisamarkandsogd', 'https://issuu.com/hgisamarkandsogd', 'hgisamarkandsogd'),  # wikidata:P9921 (Hilton Garden Inn Samarkand Sogd); live 200 (unknown ids 404)
    # Velog
    ('velog', 'https://velog.io/@-_-/posts', 'https://velog.io/@-_-', '-_-'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@maddoxunderwood1/posts', 'https://velog.io/@maddoxunderwood1', 'maddoxunderwood1'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@-__-', 'https://velog.io/@-__-', '-__-'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@000', 'https://velog.io/@000', '000'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@000000asterisk/posts', 'https://velog.io/@000000asterisk', '000000asterisk'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@0101/posts', 'https://velog.io/@0101', '0101'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@0143/posts', 'https://velog.io/@0143', '0143'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@0307', 'https://velog.io/@0307', '0307'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@0709', 'https://velog.io/@0709', '0709'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@m0ai', 'https://velog.io/@m0ai', 'm0ai'),  # wayback-200; live 200 (unknown ids 404)
    ('velog', 'https://velog.io/@m4ro/posts', 'https://velog.io/@m4ro', 'm4ro'),  # wayback-200; live 200 (unknown ids 404)
    # Brunch
    ('brunch', 'https://brunch.co.kr/@01c', 'https://brunch.co.kr/@01c', '01c'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@000080859ed7404', 'https://brunch.co.kr/@000080859ed7404', '000080859ed7404'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@00-01', 'https://brunch.co.kr/@00-01', '00-01'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@00100', 'https://brunch.co.kr/@00100', '00100'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@00-one', 'https://brunch.co.kr/@00-one', '00-one'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@s3g', 'https://brunch.co.kr/@s3g', 's3g'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@s68', 'https://brunch.co.kr/@s68', 's68'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@00mm', 'https://brunch.co.kr/@00mm', '00mm'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@0131', 'https://brunch.co.kr/@0131', '0131'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@m06b', 'https://brunch.co.kr/@m06b', 'm06b'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@ma6n', 'https://brunch.co.kr/@ma6n', 'ma6n'),  # wayback-200; live 302
    ('brunch', 'https://brunch.co.kr/@00jhj', 'https://brunch.co.kr/@00jhj', '00jhj'),  # wayback-200; live 302
    # Ameba Blog
    ('ameblo', 'http://ameblo.jp/m------------------i', 'https://ameblo.jp/m------------------i', 'm------------------i'),  # wayback-200; live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/386/', 'https://ameblo.jp/386', '386'),  # wikidata:P3502 (Hiroki Miyamura); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/12gitrmio/', 'https://ameblo.jp/12gitrmio', '12gitrmio'),  # wikidata:P3502 (MIO); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/737/', 'https://ameblo.jp/737', '737'),  # wikidata:P3502 (Nacil); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/gow/', 'https://ameblo.jp/gow', 'gow'),  # wikidata:P3502 (Maria Theresa Gow); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/mase/', 'https://ameblo.jp/mase', 'mase'),  # wikidata:P3502 (Masayoshi Mase); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/igua/', 'https://ameblo.jp/igua', 'igua'),  # wikidata:P3502 (Igua); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/scho/', 'https://ameblo.jp/scho', 'scho'),  # wikidata:P3502 (Q59135224); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/herc/', 'https://ameblo.jp/herc', 'herc'),  # wikidata:P3502 (Koji Hatta); live 200 (unknown ids 404)
    ('ameblo', 'https://ameblo.jp/9-03/', 'https://ameblo.jp/9-03', '9-03'),  # wikidata:P3502 (Keita Obara); live 200 (unknown ids 404)
    # Hatena Blog
    ('hatena_blog', 'http://www1.hatenablog.com/', 'https://www1.hatenablog.com', 'www1'),  # wayback-200; live 200 (unknown ids 404)
    ('hatena_blog', 'http://www6.hatenablog.com/', 'https://www6.hatenablog.com', 'www6'),  # wayback-200; live 200 (unknown ids 404)
    ('hatena_blog', 'http://www3.hateblo.jp/', 'https://www3.hatenablog.com', 'www3'),  # wayback-200; live 200 (unknown ids 404)
    ('hatena_blog', 'http://www123.hatenablog.com/', 'https://www123.hatenablog.com', 'www123'),  # wayback-200; live 200 (unknown ids 404)
    ('hatena_blog', 'https://goodpatch-tech.hatenablog.com', 'https://goodpatch-tech.hatenablog.com', 'goodpatch-tech'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://go-drive-tech.hatenablog.com', 'https://go-drive-tech.hatenablog.com', 'go-drive-tech'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://jmty-tech.hatenablog.com', 'https://jmty-tech.hatenablog.com', 'jmty-tech'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://engineer-techblogs.hatenablog.com', 'https://engineer-techblogs.hatenablog.com', 'engineer-techblogs'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://itechblog.hatenablog.com', 'https://itechblog.hatenablog.com', 'itechblog'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://toritony.hatenablog.com', 'https://toritony.hatenablog.com', 'toritony'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://kyomu-cycle.hatenablog.com', 'https://kyomu-cycle.hatenablog.com', 'kyomu-cycle'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    ('hatena_blog', 'https://blog.hatenablog.com', 'https://blog.hatenablog.com', 'blog'),  # web:websearch site:hatenablog.com; live 200 (unknown ids 404)
    # Dzen
    ('dzen', 'https://dzen.ru/s24', 'https://dzen.ru/s24', 's24'),  # wayback-200; live 200
    ('dzen', 'https://dzen.ru/id/5a11dcafe86a9efb372ff652', 'https://dzen.ru/id/5a11dcafe86a9efb372ff652', None),  # wikidata:P8816 (Semyon Pegov); live 200
    ('dzen', 'https://dzen.ru/m-a-arch.space', 'https://dzen.ru/m-a-arch.space', 'm-a-arch.space'),  # wayback-200; live 200
    ('dzen', 'https://dzen.ru/s-info.ru', 'https://dzen.ru/s-info.ru', 's-info.ru'),  # wayback-200; live 200
    ('dzen', 'https://dzen.ru/k_dikusar', 'https://dzen.ru/k_dikusar', 'k_dikusar'),  # wayback-200; live 200
    ('dzen', 'https://dzen.ru/id/5cc98d53a8ac8300b349356b', 'https://dzen.ru/id/5cc98d53a8ac8300b349356b', None),  # wikidata:P8816 (Skillbox); live 200
    ('dzen', 'https://dzen.ru/Instasamka', 'https://dzen.ru/Instasamka', 'Instasamka'),  # wikidata:P8816 (Instasamka); live 200
    ('dzen', 'https://dzen.ru/q', 'https://dzen.ru/q', 'q'),  # wikidata:P8816 (Yandex.Question); live 200
    ('dzen', 'https://dzen.ru/vm', 'https://dzen.ru/vm', 'vm'),  # wikidata:P8816 (Vechernyaya Moskva); live 200
    ('dzen', 'https://dzen.ru/iz', 'https://dzen.ru/iz', 'iz'),  # wikidata:P8816 (Izvestia); live 200
    ('dzen', 'https://dzen.ru/mot', 'https://dzen.ru/mot', 'mot'),  # wikidata:P8816 (Mot); live 200
    ('dzen', 'https://dzen.ru/guu', 'https://dzen.ru/guu', 'guu'),  # wikidata:P8816 (State University of Management); live 200
    # OK.ru
    ('ok_ru', 'https://ok.ru/profile/572733725036', 'https://ok.ru/profile/572733725036', '572733725036'),  # wikidata:P9269 (Paustovskiy's museum); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/119866699', 'https://ok.ru/profile/119866699', '119866699'),  # wikidata:P9269 (Andrey Davankov); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/507069610845', 'https://ok.ru/profile/507069610845', '507069610845'),  # wikidata:P9269 (Yaroslav Lisobey); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/589286715053', 'https://ok.ru/profile/589286715053', '589286715053'),  # wikidata:P9269 (Natalie Lyalina); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/571289088261', 'https://ok.ru/profile/571289088261', '571289088261'),  # wikidata:P9269 (Gulbahar Shakirova); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/168294614833', 'https://ok.ru/profile/168294614833', '168294614833'),  # wikidata:P9269 (Nonna Akhperjanyan); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/451391759779', 'https://ok.ru/profile/451391759779', '451391759779'),  # wikidata:P9269 (Q133854924); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/460563895492', 'https://ok.ru/profile/460563895492', '460563895492'),  # wikidata:P9269 (Vitaly Valentinovich Milonov); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/107759358676', 'https://ok.ru/profile/107759358676', '107759358676'),  # wikidata:P9269 (Boris Nadezhdin); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/531241630300', 'https://ok.ru/profile/531241630300', '531241630300'),  # wikidata:P9269 (Angelina Shkatova); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/570678431716', 'https://ok.ru/profile/570678431716', '570678431716'),  # wikidata:P9269 (SERB); live 200 (unknown ids 404)
    ('ok_ru', 'https://ok.ru/profile/115186435439', 'https://ok.ru/profile/115186435439', '115186435439'),  # wikidata:P9269 (Konstantin Kazenin); live 200 (unknown ids 404)
    # ShareChat
    ('sharechat', 'https://sharechat.com/profile/0j?referer=tagTrendingFeed', 'https://sharechat.com/profile/0j', '0j'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/000000000000ooo', 'https://sharechat.com/profile/000000000000ooo', '000000000000ooo'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/saanvi-reddy-1765641554-1919', 'https://sharechat.com/profile/saanvi-reddy-1765641554-1919', 'saanvi-reddy-1765641554-1919'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/1000219512', 'https://sharechat.com/profile/1000219512', '1000219512'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/0000000000harr?referer=trendingFeed', 'https://sharechat.com/profile/0000000000harr', '0000000000harr'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/MalayalamNEWJ', 'https://sharechat.com/profile/MalayalamNEWJ', 'MalayalamNEWJ'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/s', 'https://sharechat.com/profile/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/ka', 'https://sharechat.com/profile/ka', 'ka'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/00hi', 'https://sharechat.com/profile/00hi', '00hi'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/101064862', 'https://sharechat.com/profile/101064862', '101064862'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/101985069?referer=tagTrendingFeed', 'https://sharechat.com/profile/101985069', '101985069'),  # wayback-200; live 200 (unknown ids 404)
    ('sharechat', 'https://sharechat.com/profile/1026481441?d=n', 'https://sharechat.com/profile/1026481441', '1026481441'),  # wayback-200; live 200 (unknown ids 404)
    # Mercari
    ('mercari', 'https://jp.mercari.com/user/profile/1', 'https://jp.mercari.com/user/profile/1', '1'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100178874452720009471', 'https://jp.mercari.com/user/profile/100178874452720009471', '100178874452720009471'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/00000000', 'https://jp.mercari.com/user/profile/00000000', '00000000'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/101', 'https://jp.mercari.com/user/profile/101', '101'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/102', 'https://jp.mercari.com/user/profile/102', '102'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/02260534', 'https://jp.mercari.com/user/profile/02260534', '02260534'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100000746', 'https://jp.mercari.com/user/profile/100000746', '100000746'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100001197', 'https://jp.mercari.com/user/profile/100001197', '100001197'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100010039', 'https://jp.mercari.com/user/profile/100010039', '100010039'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100016440', 'https://jp.mercari.com/user/profile/100016440', '100016440'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100018397', 'https://jp.mercari.com/user/profile/100018397', '100018397'),  # wayback-200; live 200
    ('mercari', 'https://jp.mercari.com/user/profile/100018698', 'https://jp.mercari.com/user/profile/100018698', '100018698'),  # wayback-200; live 200
    # Vinted
    ('vinted', 'https://www.vinted.com/member/1-ajanauskas', 'https://www.vinted.com/member/1', '1'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100006129', 'https://www.vinted.com/member/100006129', '100006129'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/1000476-morganenv', 'https://www.vinted.com/member/1000476', '1000476'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100118129', 'https://www.vinted.com/member/100118129', '100118129'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100306188-leoninfa', 'https://www.vinted.com/member/100306188', '100306188'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100385340', 'https://www.vinted.com/member/100385340', '100385340'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100479499-magictimesshirts', 'https://www.vinted.com/member/100479499', '100479499'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100564133', 'https://www.vinted.com/member/100564133', '100564133'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100656248-holliehinchliffe', 'https://www.vinted.com/member/100656248', '100656248'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100759025-12thirty', 'https://www.vinted.com/member/100759025', '100759025'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100875855', 'https://www.vinted.com/member/100875855', '100875855'),  # wayback-200; live 200 (unknown ids 404)
    ('vinted', 'https://www.vinted.com/member/100962412', 'https://www.vinted.com/member/100962412', '100962412'),  # wayback-200; live 200 (unknown ids 404)
    # XING
    ('xing', 'https://www.xing.com/profile/M%C2%AAAlejandra_RiveroKozman', 'https://www.xing.com/profile/M%C2%AAAlejandra_RiveroKozman', 'M%C2%AAAlejandra_RiveroKozman'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/m%C2%AA_Carmen', 'https://www.xing.com/profile/m%C2%AA_Carmen', 'm%C2%AA_Carmen'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'https://www.xing.com/profile/Eva_Lips', 'https://www.xing.com/profile/Eva_Lips', 'Eva_Lips'),  # wikidata:P7176 (Eva Lips); live 200 (unknown ids 404)
    ('xing', 'https://www.xing.com/profile/Luca_Dini', 'https://www.xing.com/profile/Luca_Dini', 'Luca_Dini'),  # wikidata:P7176 (Luca Dini); live 200 (unknown ids 404)
    ('xing', 'https://www.xing.com/profile/Uwe_Krell', 'https://www.xing.com/profile/Uwe_Krell', 'Uwe_Krell'),  # wikidata:P7176 (Uwe Krell); live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/M%C2%AAALBA_OLIVA2', 'https://www.xing.com/profile/M%C2%AAALBA_OLIVA2', 'M%C2%AAALBA_OLIVA2'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/M%c2%aaBegona_MorejonHuerta', 'https://www.xing.com/profile/M%c2%aaBegona_MorejonHuerta', 'M%c2%aaBegona_MorejonHuerta'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/M%c2%aadelCARMEN_GOMEZSANCHEZ', 'https://www.xing.com/profile/M%c2%aadelCARMEN_GOMEZSANCHEZ', 'M%c2%aadelCARMEN_GOMEZSANCHEZ'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/M%C2%AAElena_DaquintasGordillo', 'https://www.xing.com/profile/M%C2%AAElena_DaquintasGordillo', 'M%C2%AAElena_DaquintasGordillo'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/M%C2%AAJose_ArroyoHurtado', 'https://www.xing.com/profile/M%C2%AAJose_ArroyoHurtado', 'M%C2%AAJose_ArroyoHurtado'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'http://www.xing.com/profile/S_Doser', 'https://www.xing.com/profile/S_Doser', 'S_Doser'),  # wayback-200; live 200 (unknown ids 404)
    ('xing', 'https://www.xing.com/profile/Sa_Aw', 'https://www.xing.com/profile/Sa_Aw', 'Sa_Aw'),  # wayback-200; live 200 (unknown ids 404)
    # Malt
    ('malt', 'https://www.malt.fr/profile/%C3%B8ceaneleroy', 'https://www.malt.fr/profile/%C3%B8ceaneleroy', '%C3%B8ceaneleroy'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/%E4%BA%9A%E5%93%81%E6%9D%8E', 'https://www.malt.fr/profile/%E4%BA%9A%E5%93%81%E6%9D%8E', '%E4%BA%9A%E5%93%81%E6%9D%8E'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/%C3%B8topplomberieservices', 'https://www.malt.fr/profile/%C3%B8topplomberieservices', '%C3%B8topplomberieservices'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/01mars', 'https://www.malt.fr/profile/01mars', '01mars'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/sa', 'https://www.malt.fr/profile/sa', 'sa'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/kam', 'https://www.malt.fr/profile/kam', 'kam'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/40ob', 'https://www.malt.fr/profile/40ob', '40ob'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/9fev', 'https://www.malt.fr/profile/9fev', '9fev'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/mabu', 'https://www.malt.fr/profile/mabu', 'mabu'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/kaes', 'https://www.malt.fr/profile/kaes', 'kaes'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/kais?q=Facebook+pixel+tracking&searchid=63cca2ad2ed75b0fc835efd3', 'https://www.malt.fr/profile/kais', 'kais'),  # wayback-200; live check blocked (403)
    ('malt', 'https://www.malt.fr/profile/24hwd', 'https://www.malt.fr/profile/24hwd', '24hwd'),  # wayback-200; live check blocked (403)
    # Komoot
    ('komoot', 'https://www.komoot.com/user/mbh', 'https://www.komoot.com/user/mbh', 'mbh'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/mabicycletteenprovence', 'https://www.komoot.com/user/mabicycletteenprovence', 'mabicycletteenprovence'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/1000042744084?width=28&height=28&crop=true&q=70', 'https://www.komoot.com/user/1000042744084', '1000042744084'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/00schneiderhh', 'https://www.komoot.com/user/00schneiderhh', '00schneiderhh'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/mdv', 'https://www.komoot.com/user/mdv', 'mdv'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/sbb', 'https://www.komoot.com/user/sbb', 'sbb'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/shi', 'https://www.komoot.com/user/shi', 'shi'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/kad', 'https://www.komoot.com/user/kad', 'kad'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/kdt', 'https://www.komoot.com/user/kdt', 'kdt'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/mamu', 'https://www.komoot.com/user/mamu', 'mamu'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/mbuk', 'https://www.komoot.com/user/mbuk', 'mbuk'),  # wayback-200; live 200 (unknown ids 404)
    ('komoot', 'https://www.komoot.com/user/md72', 'https://www.komoot.com/user/md72', 'md72'),  # wayback-200; live 200 (unknown ids 404)
    # note
    ('note_com', 'https://note.com/xqq', 'https://note.com/xqq', 'xqq'),  # wikidata:P11401 (XQQ); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/kitabata_pianist', 'https://note.com/kitabata_pianist', 'kitabata_pianist'),  # wikidata:P11401 (Yoshito Kitabata); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/unext_co', 'https://note.com/unext_co', 'unext_co'),  # wikidata:P11401 (U-NEXT Co., Ltd.); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/19460501', 'https://note.com/19460501', '19460501'),  # wikidata:P11401 (Bunka Tsushinsha); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/3tani34ro', 'https://note.com/3tani34ro', '3tani34ro'),  # wikidata:P11401 (Sanshiro Mitani); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/ebs', 'https://note.com/ebs', 'ebs'),  # wikidata:P11401 (Masaharu Yoshioka); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/pm3', 'https://note.com/pm3', 'pm3'),  # wikidata:P11401 (Tatekawa Dankichi); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/tver', 'https://note.com/tver', 'tver'),  # wikidata:P11401 (TVer); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/skeb', 'https://note.com/skeb', 'skeb'),  # wikidata:P11401 (Skeb); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/tryz', 'https://note.com/tryz', 'tryz'),  # wikidata:P11401 (Q11263339); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/bxjp', 'https://note.com/bxjp', 'bxjp'),  # wikidata:P11401 (Barubora); live 200 (unknown ids 404)
    ('note_com', 'https://note.com/kdcl', 'https://note.com/kdcl', 'kdcl'),  # wikidata:P11401 (Kidocala Ohmichi); live 200 (unknown ids 404)
    # Naver Blog
    ('naver_blog', 'https://blog.naver.com/m-03g_luna', 'https://blog.naver.com/m-03g_luna', 'm-03g_luna'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/s--__', 'https://blog.naver.com/s--__', 's--__'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-305', 'https://blog.naver.com/m-305', 'm-305'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'http://blog.naver.com/m-a-p', 'https://blog.naver.com/m-a-p', 'm-a-p'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-b-b', 'https://blog.naver.com/m-b-b', 'm-b-b'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'http://blog.naver.com/m-car?', 'https://blog.naver.com/m-car', 'm-car'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-key', 'https://blog.naver.com/m-key', 'm-key'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-ppt', 'https://blog.naver.com/m-ppt', 'm-ppt'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/s--th', 'https://blog.naver.com/s--th', 's--th'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-2030?proxyReferer=http%3A%2F%2Fm-2030.blog.me%2F', 'https://blog.naver.com/m-2030', 'm-2030'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-9pyv', 'https://blog.naver.com/m-9pyv', 'm-9pyv'),  # wayback-200; live 200 (unknown ids 404)
    ('naver_blog', 'https://blog.naver.com/m-a-t-t-e-r', 'https://blog.naver.com/m-a-t-t-e-r', 'm-a-t-t-e-r'),  # wayback-200; live 200 (unknown ids 404)
    # Mixcloud
    ('mixcloud', 'https://www.mixcloud.com/M%C2%B2Squared/', 'https://www.mixcloud.com/M%C2%B2Squared', 'M%C2%B2Squared'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'http://www.mixcloud.com/m/', 'https://www.mixcloud.com/m', 'm'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/m%C3%A1rcia-lorenzoni/', 'https://www.mixcloud.com/m%C3%A1rcia-lorenzoni', 'm%C3%A1rcia-lorenzoni'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/m%C3%A0o-chi%E1%BA%BFn/', 'https://www.mixcloud.com/m%C3%A0o-chi%E1%BA%BFn', 'm%C3%A0o-chi%E1%BA%BFn'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/M%C3%8DSTIC_DISCS/', 'https://www.mixcloud.com/M%C3%8DSTIC_DISCS', 'M%C3%8DSTIC_DISCS'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/3x3cute/', 'https://www.mixcloud.com/3x3cute', '3x3cute'),  # wikidata:P9509 (3x3cute); live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/M%C2%B52/', 'https://www.mixcloud.com/M%C2%B52', 'M%C2%B52'),  # wayback-200; live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/gss/', 'https://www.mixcloud.com/gss', 'gss'),  # wikidata:P9509 (Remi Kabaka Jr); live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/2xT/', 'https://www.mixcloud.com/2xT', '2xT'),  # wikidata:P9509 (Thomas Thyssen); live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/ty1/', 'https://www.mixcloud.com/ty1', 'ty1'),  # wikidata:P9509 (TY1); live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/slam/', 'https://www.mixcloud.com/slam', 'slam'),  # wikidata:P9509 (Slam); live check blocked (403)
    ('mixcloud', 'https://www.mixcloud.com/Moby/', 'https://www.mixcloud.com/Moby', 'Moby'),  # wikidata:P9509 (Moby); live check blocked (403)
    # Audiomack
    ('audiomack', 'https://audiomack.com/m', 'https://audiomack.com/m', 'm'),  # wayback-200; live 200
    ('audiomack', 'https://audiomack.com/m-a-d-e-b-y-t-h-e-s-o-n', 'https://audiomack.com/m-a-d-e-b-y-t-h-e-s-o-n', 'm-a-d-e-b-y-t-h-e-s-o-n'),  # wayback-200; live 200
    ('audiomack', 'https://audiomack.com/m-1-muzik-1', 'https://audiomack.com/m-1-muzik-1', 'm-1-muzik-1'),  # wayback-200; live 200
    ('audiomack', 'https://audiomack.com/k-boy_izi', 'https://audiomack.com/k-boy_izi', 'k-boy_izi'),  # wayback-200; live 200
    ('audiomack', 'https://audiomack.com/79942327', 'https://audiomack.com/79942327', '79942327'),  # wikidata:P13527 (Mr Joel Joseph); live 200
    ('audiomack', 'https://audiomack.com/69de3722269bf', 'https://audiomack.com/69de3722269bf', '69de3722269bf'),  # wikidata:P13527 (Mel Diaz); live 200
    ('audiomack', 'https://audiomack.com/M-honey', 'https://audiomack.com/M-honey', 'M-honey'),  # wayback-200; live 200
    ('audiomack', 'https://audiomack.com/upy', 'https://audiomack.com/upy', 'upy'),  # wikidata:P13527 (Q139741245); live 200
    ('audiomack', 'https://audiomack.com/matt', 'https://audiomack.com/matt', 'matt'),  # wikidata:P13527 (Matt); live 200
    ('audiomack', 'https://audiomack.com/ebbb', 'https://audiomack.com/ebbb', 'ebbb'),  # wikidata:P13527 (Q136682676); live 200
    ('audiomack', 'https://audiomack.com/bulow', 'https://audiomack.com/bulow', 'bulow'),  # wikidata:P13527 (bülow); live 200
    ('audiomack', 'https://audiomack.com/hexed', 'https://audiomack.com/hexed', 'hexed'),  # wikidata:P13527 (HEXED); live 200
    # BitChute
    ('bitchute', 'https://www.bitchute.com/channel/...', 'https://www.bitchute.com/channel/...', '...'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/-critical-thinker-/', 'https://www.bitchute.com/channel/-critical-thinker-', '-critical-thinker-'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/01cQ...', 'https://www.bitchute.com/channel/01cQ...', '01cQ...'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/-aile-/', 'https://www.bitchute.com/channel/-aile-', '-aile-'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/-soy_magnus-/', 'https://www.bitchute.com/channel/-soy_magnus-', '-soy_magnus-'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/02070412/', 'https://www.bitchute.com/channel/02070412', '02070412'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/000v000/', 'https://www.bitchute.com/channel/000v000', '000v000'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/005b1Yfu5LBx/', 'https://www.bitchute.com/channel/005b1Yfu5LBx', '005b1Yfu5LBx'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/k/', 'https://www.bitchute.com/channel/k', 'k'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/03/', 'https://www.bitchute.com/channel/03', '03'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/k-a/', 'https://www.bitchute.com/channel/k-a', 'k-a'),  # wayback-200; live 200
    ('bitchute', 'https://www.bitchute.com/channel/0618/', 'https://www.bitchute.com/channel/0618', '0618'),  # wayback-200; live 200
    # LINE
    ('line', 'https://page.line.me/m-m.3-28?openQrModal=true', 'https://page.line.me/m-m.3-28', 'm-m.3-28'),  # wayback-200; live 200 (unknown ids 404)
    ('line', 'https://page.line.me/m-box?openQrModal=true', 'https://page.line.me/m-box', 'm-box'),  # wayback-200; live 200 (unknown ids 404)
    ('line', 'https://page.line.me/m.a.d_sports_gym?openQrModal=true', 'https://page.line.me/m.a.d_sports_gym', 'm.a.d_sports_gym'),  # wayback-200; live 200 (unknown ids 404)
    ('line', 'https://page.line.me/308vtbmv', 'https://page.line.me/308vtbmv', '308vtbmv'),  # wikidata:P14244 (Himari); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/Gero', 'https://page.line.me/Gero', 'Gero'),  # wikidata:P14244 (Gero); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/line', 'https://page.line.me/line', 'line'),  # wikidata:P14244 (LINE); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/lead', 'https://page.line.me/lead', 'lead'),  # wikidata:P14244 (Lead); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/nagi', 'https://page.line.me/nagi', 'nagi'),  # wikidata:P14244 (Nagi); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/miro', 'https://page.line.me/miro', 'miro'),  # wikidata:P14244 (miro); live 200 (unknown ids 404)
    ('line', 'https://page.line.me/njpw', 'https://page.line.me/njpw', 'njpw'),  # wikidata:P14244 (New Japan Pro-Wrestling); live 200 (unknown ids 404)
    # KakaoTalk Channel
    ('kakaotalk_channel', 'https://pf.kakao.com/_aAxmxnn3.', 'https://pf.kakao.com/_aAxmxnn3.', 'aAxmxnn3.'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_1004-pay/chat', 'https://pf.kakao.com/_1004-pay', '1004-pay'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/__fyxgxin', 'https://pf.kakao.com/__fyxgxin', '_fyxgxin'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_00000', 'https://pf.kakao.com/_00000', '00000'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_301S', 'https://pf.kakao.com/_301S', '301S'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/__xahbJG/chat', 'https://pf.kakao.com/__xahbJG', '_xahbJG'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_1', 'https://pf.kakao.com/_1', '1'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_A', 'https://pf.kakao.com/_A', 'A'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_s', 'https://pf.kakao.com/_s', 's'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_k', 'https://pf.kakao.com/_k', 'k'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_abcd', 'https://pf.kakao.com/_abcd', 'abcd'),  # wayback-200; live 200
    ('kakaotalk_channel', 'https://pf.kakao.com/_...', 'https://pf.kakao.com/_...', '...'),  # wayback-200; live check failed
    # Tripadvisor
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/k1r', 'https://www.tripadvisor.com/Profile/k1r', 'k1r'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M-Duggal_Himachal', 'https://www.tripadvisor.com/Profile/M-Duggal_Himachal', 'M-Duggal_Himachal'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M-A-Etman', 'https://www.tripadvisor.com/Profile/M-A-Etman', 'M-A-Etman'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M-F_Trackers', 'https://www.tripadvisor.com/Profile/M-F_Trackers', 'M-F_Trackers'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M-Alqaseer', 'https://www.tripadvisor.com/Profile/M-Alqaseer', 'M-Alqaseer'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M-P7', 'https://www.tripadvisor.com/Profile/M-P7', 'M-P7'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M0ab', 'https://www.tripadvisor.com/Profile/M0ab', 'M0ab'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/m0c1', 'https://www.tripadvisor.com/Profile/m0c1', 'm0c1'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/m0ec', 'https://www.tripadvisor.com/Profile/m0ec', 'm0ec'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/M0fi', 'https://www.tripadvisor.com/Profile/M0fi', 'M0fi'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/m0re', 'https://www.tripadvisor.com/Profile/m0re', 'm0re'),  # wayback-200; live 200
    ('tripadvisor', 'https://www.tripadvisor.com/Profile/s033', 'https://www.tripadvisor.com/Profile/s033', 's033'),  # wayback-200; live 200
    # Contra
    ('contra', 'https://contra.com/m2547392_mccy6dzx/work', 'https://contra.com/m2547392_mccy6dzx', 'm2547392_mccy6dzx'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/m2interactive_0h5qobsf/work', 'https://contra.com/m2interactive_0h5qobsf', 'm2interactive_0h5qobsf'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/MadDigital/work', 'https://contra.com/MadDigital', 'MadDigital'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/madi', 'https://contra.com/madi', 'madi'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/kajabi', 'https://contra.com/kajabi', 'kajabi'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/kaitlyn', 'https://contra.com/kaitlyn', 'kaitlyn'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/m0000320', 'https://contra.com/m0000320', 'm0000320'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/m4tyn000', 'https://contra.com/m4tyn000', 'm4tyn000'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/mabogale/work', 'https://contra.com/mabogale', 'mabogale'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/madison2', 'https://contra.com/madison2', 'madison2'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/KahinurA/work', 'https://contra.com/KahinurA', 'KahinurA'),  # wayback-200; live 200 (unknown ids 404)
    ('contra', 'https://contra.com/kaiensa0', 'https://contra.com/kaiensa0', 'kaiensa0'),  # wayback-200; live 200 (unknown ids 404)
    # Codementor
    ('codementor', 'https://www.codementor.io/@a-b', 'https://www.codementor.io/@a-b', 'a-b'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@a.k', 'https://www.codementor.io/@a.k', 'a.k'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@_lutfor', 'https://www.codementor.io/@_lutfor', '_lutfor'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@000707', 'https://www.codementor.io/@000707', '000707'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@009bet', 'https://www.codementor.io/@009bet', '009bet'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@42pe', 'https://www.codementor.io/@42pe', '42pe'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@789p', 'https://www.codementor.io/@789p', '789p'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@8344', 'https://www.codementor.io/@8344', '8344'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@888p', 'https://www.codementor.io/@888p', '888p'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@000993', 'https://www.codementor.io/@000993', '000993'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@123b2cnet', 'https://www.codementor.io/@123b2cnet', '123b2cnet'),  # wayback-200; live 200 (unknown ids 404)
    ('codementor', 'https://www.codementor.io/@13ebetorg', 'https://www.codementor.io/@13ebetorg', '13ebetorg'),  # wayback-200; live 200 (unknown ids 404)
    # Trakt
    ('trakt', 'https://app.trakt.tv/profile/me', 'https://app.trakt.tv/profile/me', 'me'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/andrei-l-magnea?mode=media', 'https://app.trakt.tv/profile/andrei-l-magnea', 'andrei-l-magnea'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/leigh.riggs.2025', 'https://app.trakt.tv/profile/leigh.riggs.2025', 'leigh.riggs.2025'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/aniela-krajewska', 'https://app.trakt.tv/profile/aniela-krajewska', 'aniela-krajewska'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/hannah_gbs', 'https://app.trakt.tv/profile/hannah_gbs', 'hannah_gbs'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/0rsalah', 'https://app.trakt.tv/profile/0rsalah', '0rsalah'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/Magnus-G?mode=show', 'https://app.trakt.tv/profile/Magnus-G', 'Magnus-G'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/qlum', 'https://app.trakt.tv/profile/qlum', 'qlum'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/sean', 'https://app.trakt.tv/profile/sean', 'sean'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/hgram', 'https://app.trakt.tv/profile/hgram', 'hgram'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/julif', 'https://app.trakt.tv/profile/julif', 'julif'),  # wayback-200; live 200
    ('trakt', 'https://app.trakt.tv/profile/lieen', 'https://app.trakt.tv/profile/lieen', 'lieen'),  # wayback-200; live 200
    # Minds
    ('minds', 'https://www.minds.com/K', 'https://www.minds.com/K', 'K'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/K3ybladewielder', 'https://www.minds.com/K3ybladewielder', 'K3ybladewielder'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/m.e.a.g.a.n', 'https://www.minds.com/m.e.a.g.a.n', 'm.e.a.g.a.n'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/k-mil', 'https://www.minds.com/k-mil', 'k-mil'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/m_ark', 'https://www.minds.com/m_ark', 'm_ark'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/M0rTuS', 'https://www.minds.com/M0rTuS', 'M0rTuS'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/m00t', 'https://www.minds.com/m00t', 'm00t'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/M11S', 'https://www.minds.com/M11S', 'M11S'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/ma33', 'https://www.minds.com/ma33', 'ma33'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/s.ex', 'https://www.minds.com/s.ex', 's.ex'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/s474/', 'https://www.minds.com/s474', 's474'),  # wayback-200; live 200
    ('minds', 'https://www.minds.com/saak', 'https://www.minds.com/saak', 'saak'),  # wayback-200; live 200
    # Kickstarter
    ('kickstarter', 'https://www.kickstarter.com/profile/-a-', 'https://www.kickstarter.com/profile/-a-', '-a-'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/-vision-prime-1', 'https://www.kickstarter.com/profile/-vision-prime-1', '-vision-prime-1'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/-3d-fortress-', 'https://www.kickstarter.com/profile/-3d-fortress-', '-3d-fortress-'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/1', 'https://www.kickstarter.com/profile/1', '1'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/0-hr', 'https://www.kickstarter.com/profile/0-hr', '0-hr'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'http://www.kickstarter.com/profile/MablesMagic', 'https://www.kickstarter.com/profile/MablesMagic', 'MablesMagic'),  # wayback-200; live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/iga', 'https://www.kickstarter.com/profile/iga', 'iga'),  # wikidata:P9271 (Koji Igarashi); live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/mde', 'https://www.kickstarter.com/profile/mde', 'mde'),  # wikidata:P9271 (Sam Hyde); live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/cig', 'https://www.kickstarter.com/profile/cig', 'cig'),  # wikidata:P9271 (Cloud Imperium Games); live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/vldl', 'https://www.kickstarter.com/profile/vldl', 'vldl'),  # wikidata:P9271 (Viva La Dirt League); live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/6502b', 'https://www.kickstarter.com/profile/6502b', '6502b'),  # wikidata:P9271 (Q107998861); live check blocked (403)
    ('kickstarter', 'https://www.kickstarter.com/profile/ysnet', 'https://www.kickstarter.com/profile/ysnet', 'ysnet'),  # wikidata:P9271 (Ys Net); live check blocked (403)
    # Packagist
    ('packagist', 'https://packagist.org/users/%E4%BB%A3%E7%A0%81%E6%90%AC%E8%BF%90%E5%B7%A5/', 'https://packagist.org/users/%E4%BB%A3%E7%A0%81%E6%90%AC%E8%BF%90%E5%B7%A5', '%E4%BB%A3%E7%A0%81%E6%90%AC%E8%BF%90%E5%B7%A5'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/%E7%A7%80%E6%89%8D/', 'https://packagist.org/users/%E7%A7%80%E6%89%8D', '%E7%A7%80%E6%89%8D'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/a.milenin/', 'https://packagist.org/users/a.milenin', 'a.milenin'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/-jason/', 'https://packagist.org/users/-jason', '-jason'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/_alK13/', 'https://packagist.org/users/_alK13', '_alK13'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/0001000xyz/', 'https://packagist.org/users/0001000xyz', '0001000xyz'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/00F100/', 'https://packagist.org/users/00F100', '00F100'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/Sachin%20Agarwal/', 'https://packagist.org/users/Sachin%20Agarwal', 'Sachin%20Agarwal'),  # wayback-200; live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/nijel', 'https://packagist.org/users/nijel', 'nijel'),  # wikidata:P11531 (Michal Čihař); live 200 (unknown ids 404)
    ('packagist', 'https://packagist.org/users/taavi', 'https://packagist.org/users/taavi', 'taavi'),  # wikidata:P11531 (Q118521440); live 200 (unknown ids 404)
    # Slashdot
    ('slashdot', 'http://slashdot.org/~%C5nubis/', 'https://slashdot.org/~%C5nubis', '%C5nubis'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~-1/', 'https://slashdot.org/~-1', '-1'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~%2B%2BCaChElInKeR%2B%2B', 'https://slashdot.org/~%2B%2BCaChElInKeR%2B%2B', '%2B%2BCaChElInKeR%2B%2B'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~%2BA.OS.L.S_Bozo%2B', 'https://slashdot.org/~%2BA.OS.L.S_Bozo%2B', '%2BA.OS.L.S_Bozo%2B'),  # wayback-200; live check blocked (403)
    ('slashdot', 'https://slashdot.org/~%2B_-repo-_%2B', 'https://slashdot.org/~%2B_-repo-_%2B', '%2B_-repo-_%2B'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~-_broken_watchman_-', 'https://slashdot.org/~-_broken_watchman_-', '-_broken_watchman_-'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~-%3D%5B%20SYRiNX%20%5D%3D-/', 'https://slashdot.org/~-%3D%5B%20SYRiNX%20%5D%3D-', '-%3D%5B%20SYRiNX%20%5D%3D-'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~%23define/', 'https://slashdot.org/~%23define', '%23define'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~K./', 'https://slashdot.org/~K.', 'K.'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~M&M/', 'https://slashdot.org/~M&M', 'M&M'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~M-2/', 'https://slashdot.org/~M-2', 'M-2'),  # wayback-200; live check blocked (403)
    ('slashdot', 'http://slashdot.org/~M-G/', 'https://slashdot.org/~M-G', 'M-G'),  # wayback-200; live check blocked (403)
    # ResearchGate
    ('researchgate', 'https://www.researchgate.net/profile/2', 'https://www.researchgate.net/profile/2', '2'),  # wikidata:P2038 (Brian K. Sullivan); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/M-A-Abd-Elgawad', 'https://www.researchgate.net/profile/M-A-Abd-Elgawad', 'M-A-Abd-Elgawad'),  # wayback-200; live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/M-A-Ahmed', 'https://www.researchgate.net/profile/M-A-Ahmed', 'M-A-Ahmed'),  # wayback-200; live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Jeff_Wagoner2', 'https://www.researchgate.net/profile/Jeff_Wagoner2', 'Jeff_Wagoner2'),  # wikidata:P2038 (Jeff Wagoner); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/47', 'https://www.researchgate.net/profile/47', '47'),  # wikidata:P2038 (Pablo Alonso-González); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/M-A-Akbarsha', 'https://www.researchgate.net/profile/M-A-Akbarsha', 'M-A-Akbarsha'),  # wayback-200; live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/C', 'https://www.researchgate.net/profile/C', 'C'),  # wikidata:P2038 (Chacko Jobichen); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Li_Zeng4', 'https://www.researchgate.net/profile/Li_Zeng4', 'Li_Zeng4'),  # wikidata:P2038 (Li Zeng); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Yu-Yin-21', 'https://www.researchgate.net/profile/Yu-Yin-21', 'Yu-Yin-21'),  # wikidata:P2038 (Yu Yin); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Waed-Dada', 'https://www.researchgate.net/profile/Waed-Dada', 'Waed-Dada'),  # wikidata:P2038 (Waed Dada); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Rama_Cont', 'https://www.researchgate.net/profile/Rama_Cont', 'Rama_Cont'),  # wikidata:P2038 (Rama Cont); live check blocked (403)
    ('researchgate', 'https://www.researchgate.net/profile/Peter-Lina', 'https://www.researchgate.net/profile/Peter-Lina', 'Peter-Lina'),  # wikidata:P2038 (Peter Lina); live check blocked (403)
    # ---- part 3 ----
    # OnlyFans
    ('onlyfans', 'https://onlyfans.com/m', 'https://onlyfans.com/m', 'm'),  # wayback-200; live 200
    ('onlyfans', 'https://onlyfans.com/m-i-s-s-j-a-c-q-u-e-s-xx', 'https://onlyfans.com/m-i-s-s-j-a-c-q-u-e-s-xx', 'm-i-s-s-j-a-c-q-u-e-s-xx'),  # wayback-200; live 200
    ('onlyfans', 'https://onlyfans.com/m.02of', 'https://onlyfans.com/m.02of', 'm.02of'),  # wayback-200; live 200
    ('onlyfans', 'http://onlyfans.com/m-', 'https://onlyfans.com/m-', 'm-'),  # wayback-200; live 200
    ('onlyfans', 'https://onlyfans.com/m.27_cannagirl', 'https://onlyfans.com/m.27_cannagirl', 'm.27_cannagirl'),  # wayback-200; live 200
    ('onlyfans', 'https://onlyfans.com/m-pkW9YE8cvMrnYJ', 'https://onlyfans.com/m-pkW9YE8cvMrnYJ', 'm-pkW9YE8cvMrnYJ'),  # wayback-200; live 200
    ('onlyfans', 'https://onlyfans.com/alus', 'https://onlyfans.com/alus', 'alus'),  # wikidata:P8604 (Alus); live 200
    ('onlyfans', 'https://onlyfans.com/emmag', 'https://onlyfans.com/emmag', 'emmag'),  # wikidata:P8604 (Emma Glover); live 200
    ('onlyfans', 'https://onlyfans.com/angela', 'https://onlyfans.com/angela', 'angela'),  # wikidata:P8604 (Angela White); live 200
    ('onlyfans', 'https://onlyfans.com/jizlee', 'https://onlyfans.com/jizlee', 'jizlee'),  # wikidata:P8604 (Jiz Lee); live 200
    ('onlyfans', 'https://onlyfans.com/daphne', 'https://onlyfans.com/daphne', 'daphne'),  # wikidata:P8604 (Daphne Summers); live 200
    ('onlyfans', 'https://onlyfans.com/Janine', 'https://onlyfans.com/Janine', 'Janine'),  # wikidata:P8604 (Janine Lindemulder); live 200
    # Open Collective
    ('opencollective', 'https://opencollective.com/m', 'https://opencollective.com/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/m-angeline-markham', 'https://opencollective.com/m-angeline-markham', 'm-angeline-markham'),  # wayback-200; live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/m-allanson', 'https://opencollective.com/m-allanson', 'm-allanson'),  # wayback-200; live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/m1st3r_t4c0', 'https://opencollective.com/m1st3r_t4c0', 'm1st3r_t4c0'),  # wayback-200; live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/mybb', 'https://opencollective.com/mybb', 'mybb'),  # wikidata:P14655 (MyBB); live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/xfce', 'https://opencollective.com/xfce', 'xfce'),  # wikidata:P14655 (Q170821); live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/tmux', 'https://opencollective.com/tmux', 'tmux'),  # wikidata:P14655 (tmux); live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/htop', 'https://opencollective.com/htop', 'htop'),  # wikidata:P14655 (htop); live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/umap', 'https://opencollective.com/umap', 'umap'),  # wikidata:P14655 (uMap); live 200 (unknown ids 404)
    ('opencollective', 'https://opencollective.com/ooni', 'https://opencollective.com/ooni', 'ooni'),  # wikidata:P14655 (Open Observatory of Network Interference); live 200 (unknown ids 404)
    # Liberapay
    ('liberapay', 'https://liberapay.com/m.2', 'https://liberapay.com/m.2', 'm.2'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/m.dacruzbizzell/', 'https://liberapay.com/m.dacruzbizzell', 'm.dacruzbizzell'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/m.ash', 'https://liberapay.com/m.ash', 'm.ash'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/m-p-3/', 'https://liberapay.com/m-p-3', 'm-p-3'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/m_raitisoja/', 'https://liberapay.com/m_raitisoja', 'm_raitisoja'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/M0N7Y5/', 'https://liberapay.com/M0N7Y5', 'M0N7Y5'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/K_/', 'https://liberapay.com/K_', 'K_'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/S1m/', 'https://liberapay.com/S1m', 'S1m'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/K0d/', 'https://liberapay.com/K0d', 'K0d'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/SAID', 'https://liberapay.com/SAID', 'SAID'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/k8ie', 'https://liberapay.com/k8ie', 'k8ie'),  # wayback-200; live check blocked (403)
    ('liberapay', 'https://liberapay.com/Kang/', 'https://liberapay.com/Kang', 'Kang'),  # wayback-200; live check blocked (403)
    # WordPress.org
    ('wordpress_org', 'https://profiles.wordpress.org/m/', 'https://profiles.wordpress.org/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'http://profiles.wordpress.org/k-productions-inc/', 'https://profiles.wordpress.org/k-productions-inc', 'k-productions-inc'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'http://profiles.wordpress.org/m-ali/', 'https://profiles.wordpress.org/m-ali', 'm-ali'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/K', 'https://profiles.wordpress.org/K', 'K'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/k-2/', 'https://profiles.wordpress.org/k-2', 'k-2'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/m-alo/', 'https://profiles.wordpress.org/m-alo', 'm-alo'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/m-azure/', 'https://profiles.wordpress.org/m-azure', 'm-azure'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'http://profiles.wordpress.org/m-b-c-4/', 'https://profiles.wordpress.org/m-b-c-4', 'm-b-c-4'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/m-e-h', 'https://profiles.wordpress.org/m-e-h', 'm-e-h'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'http://profiles.wordpress.org/s-234/', 'https://profiles.wordpress.org/s-234', 's-234'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'https://profiles.wordpress.org/s-a-n/', 'https://profiles.wordpress.org/s-a-n', 's-a-n'),  # wayback-200; live 200 (unknown ids 404)
    ('wordpress_org', 'http://profiles.wordpress.org/s-andy/', 'https://profiles.wordpress.org/s-andy', 's-andy'),  # wayback-200; live 200 (unknown ids 404)
    # Instructables
    ('instructables', 'http://www.instructables.com/member/m/', 'https://www.instructables.com/member/m', 'm'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'https://www.instructables.com/member/s-bchandramouli/', 'https://www.instructables.com/member/s-bchandramouli', 's-bchandramouli'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/S-239/', 'https://www.instructables.com/member/S-239', 'S-239'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/S-Anderson/', 'https://www.instructables.com/member/S-Anderson', 'S-Anderson'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/s/', 'https://www.instructables.com/member/s', 's'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/S-Bro/', 'https://www.instructables.com/member/S-Bro', 'S-Bro'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/K-10K/', 'https://www.instructables.com/member/K-10K', 'K-10K'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/k-673/', 'https://www.instructables.com/member/k-673', 'k-673'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/K-all/', 'https://www.instructables.com/member/K-all', 'K-all'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/K-car/', 'https://www.instructables.com/member/K-car', 'K-car'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/K-Dub/', 'https://www.instructables.com/member/K-Dub', 'K-Dub'),  # wayback-200; live 200 (unknown ids 404)
    ('instructables', 'http://www.instructables.com/member/k-esd/', 'https://www.instructables.com/member/k-esd', 'k-esd'),  # wayback-200; live 200 (unknown ids 404)
    # TMDB
    ('tmdb', 'https://www.themoviedb.org/u/s-c-h-a-t-t-e-n', 'https://www.themoviedb.org/u/s-c-h-a-t-t-e-n', 's-c-h-a-t-t-e-n'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/m.dam', 'https://www.themoviedb.org/u/m.dam', 'm.dam'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/M-Rots', 'https://www.themoviedb.org/u/M-Rots', 'M-Rots'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/s0lan_in', 'https://www.themoviedb.org/u/s0lan_in', 's0lan_in'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/M.LeMarchand', 'https://www.themoviedb.org/u/M.LeMarchand', 'M.LeMarchand'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/S231', 'https://www.themoviedb.org/u/S231', 'S231'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/s5ka', 'https://www.themoviedb.org/u/s5ka', 's5ka'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/s6kx', 'https://www.themoviedb.org/u/s6kx', 's6kx'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/k02t', 'https://www.themoviedb.org/u/k02t', 'k02t'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/m.m.j', 'https://www.themoviedb.org/u/m.m.j', 'm.m.j'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/s0nar', 'https://www.themoviedb.org/u/s0nar', 's0nar'),  # wayback-200; live 200 (unknown ids 404)
    ('tmdb', 'https://www.themoviedb.org/u/s1339', 'https://www.themoviedb.org/u/s1339', 's1339'),  # wayback-200; live 200 (unknown ids 404)
    # Hex
    ('hex_pm', 'https://hex.pm/users/0m3', 'https://hex.pm/users/0m3', '0m3'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/adamniedzielski', 'https://hex.pm/users/adamniedzielski', 'adamniedzielski'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/a.portnov', 'https://hex.pm/users/a.portnov', 'a.portnov'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/1-bit-wonder', 'https://hex.pm/users/1-bit-wonder', '1-bit-wonder'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/__red__', 'https://hex.pm/users/__red__', '__red__'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/0010', 'https://hex.pm/users/0010', '0010'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/0918nobita', 'https://hex.pm/users/0918nobita', '0918nobita'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/1ma', 'https://hex.pm/users/1ma', '1ma'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/23k', 'https://hex.pm/users/23k', '23k'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/5ht', 'https://hex.pm/users/5ht', '5ht'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/_df', 'https://hex.pm/users/_df', '_df'),  # wayback-200; live 200 (unknown ids 404)
    ('hex_pm', 'https://hex.pm/users/abs', 'https://hex.pm/users/abs', 'abs'),  # wayback-200; live 200 (unknown ids 404)
    # MetaCPAN
    ('metacpan', 'https://metacpan.org/author/AAA', 'https://metacpan.org/author/AAA', 'AAA'),  # wayback-200; live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/AADLER', 'https://metacpan.org/author/AADLER', 'AADLER'),  # wayback-200; live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/SDS', 'https://metacpan.org/author/SDS', 'SDS'),  # wikidata:P8124 (Sergio de Sousa); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/EDF', 'https://metacpan.org/author/EDF', 'EDF'),  # wikidata:P8124 (Q127329136); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/DHA', 'https://metacpan.org/author/DHA', 'DHA'),  # wikidata:P8124 (David H. Adler); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/LDS', 'https://metacpan.org/author/LDS', 'LDS'),  # wikidata:P8124 (Lincoln Stein); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/SKIM', 'https://metacpan.org/author/SKIM', 'SKIM'),  # wikidata:P8124 (Q27954834); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/LWALL', 'https://metacpan.org/author/LWALL', 'LWALL'),  # wikidata:P8124 (Larry Wall); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/JESSE', 'https://metacpan.org/author/JESSE', 'JESSE'),  # wikidata:P8124 (Jesse Vincent); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/ROCKY', 'https://metacpan.org/author/ROCKY', 'ROCKY'),  # wikidata:P8124 (R. Bernstein); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/DYFET', 'https://metacpan.org/author/DYFET', 'DYFET'),  # wikidata:P8124 (David Sugar); live check blocked (402)
    ('metacpan', 'https://metacpan.org/author/SAPER', 'https://metacpan.org/author/SAPER', 'SAPER'),  # wikidata:P8124 (Sébastien Aperghis-Tramoni); live check blocked (402)
    # Indie Hackers
    ('indiehackers', 'https://www.indiehackers.com/maciejmyslinski?id=JpeOFNgezFhhmwHGhWQqFBtfwyy1', 'https://www.indiehackers.com/maciejmyslinski', 'maciejmyslinski'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/m-design?id=Jj950TPg8xRe4HjObYJldRzoXYT2', 'https://www.indiehackers.com/m-design', 'm-design'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/M_CHICHI?id=5YQt0melFOZsvJ7lBtuCw0sWpZE2', 'https://www.indiehackers.com/M_CHICHI', 'M_CHICHI'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/M165437?id=BaKRVKO4jYTaxjlKs1dVi1iTyku1', 'https://www.indiehackers.com/M165437', 'M165437'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/mac?id=ZvTzQygh92WedD2ZJgA3Ndwlaqn1', 'https://www.indiehackers.com/mac', 'mac'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/s_m?id=PCF7cxVfqOMqA76gluwlNb3T6tt2', 'https://www.indiehackers.com/s_m', 's_m'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/kan?id=kPNH7qA43UObMAXpWjgiumIahbN2', 'https://www.indiehackers.com/kan', 'kan'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/m121', 'https://www.indiehackers.com/m121', 'm121'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/m15o', 'https://www.indiehackers.com/m15o', 'm15o'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/m1aw?id=wzquQMqX2cfsUX2kJQ2diXNUuaU2', 'https://www.indiehackers.com/m1aw', 'm1aw'),  # wayback-200; live 200 (unknown ids 404)
    ('indiehackers', 'https://www.indiehackers.com/m_ke', 'https://www.indiehackers.com/m_ke', 'm_ke'),  # wayback-200; live 200 (unknown ids 404)
    # HackerEarth
    ('hackerearth', 'https://www.hackerearth.com/@--/', 'https://www.hackerearth.com/@--', '--'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@006kirti.sharma', 'https://www.hackerearth.com/@006kirti.sharma', '006kirti.sharma'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@----/', 'https://www.hackerearth.com/@----', '----'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@0.5_seconds', 'https://www.hackerearth.com/@0.5_seconds', '0.5_seconds'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@00174/', 'https://www.hackerearth.com/@00174', '00174'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@0.vikaspandey', 'https://www.hackerearth.com/@0.vikaspandey', '0.vikaspandey'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@-Green/', 'https://www.hackerearth.com/@-Green', '-Green'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@-3/', 'https://www.hackerearth.com/@-3', '-3'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@m1/', 'https://www.hackerearth.com/@m1', 'm1'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@-17/', 'https://www.hackerearth.com/@-17', '-17'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerearth', 'https://www.hackerearth.com/@.86', 'https://www.hackerearth.com/@.86', '.86'),  # wayback-200; live 200 (unknown ids 404)
    # Myspace
    ('myspace', 'https://myspace.com/m-inamo.com', 'https://myspace.com/m-inamo.com', 'm-inamo.com'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'http://www.myspace.com/m-0-7', 'https://myspace.com/m-0-7', 'm-0-7'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'http://www.myspace.com/s.a.h_z.s.f09', 'https://myspace.com/s.a.h_z.s.f09', 's.a.h_z.s.f09'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/2pac', 'https://myspace.com/2pac', '2pac'),  # wikidata:P3265 (Tupac Shakur); live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/u2', 'https://myspace.com/u2', 'u2'),  # wikidata:P3265 (U2); live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/ab', 'https://myspace.com/ab', 'ab'),  # wikidata:P3265 (Ab-Soul); live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/fr', 'https://myspace.com/fr', 'fr'),  # wikidata:P3265 (Sabin Todorov); live 200 (unknown ids 404)
    ('myspace', 'http://www.myspace.com/m-30', 'https://myspace.com/m-30', 'm-30'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/m-exemplar', 'https://myspace.com/m-exemplar', 'm-exemplar'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/m-j.moses', 'https://myspace.com/m-j.moses', 'm-j.moses'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'https://myspace.com/m-mathieu.chedid', 'https://myspace.com/m-mathieu.chedid', 'm-mathieu.chedid'),  # wayback-200; live 200 (unknown ids 404)
    ('myspace', 'http://www.myspace.com/s-5', 'https://myspace.com/s-5', 's-5'),  # wayback-200; live 200 (unknown ids 404)
    # About.me
    ('about_me', 'https://about.me/m.alcazar.celdran', 'https://about.me/m.alcazar.celdran', 'm.alcazar.celdran'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m.662.x', 'https://about.me/m.662.x', 'm.662.x'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m.a_kaisar', 'https://about.me/m.a_kaisar', 'm.a_kaisar'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'http://about.me/M.A.Y.A', 'https://about.me/M.A.Y.A', 'M.A.Y.A'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m-m', 'https://about.me/m-m', 'm-m'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/k.c', 'https://about.me/k.c', 'k.c'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/k.t', 'https://about.me/k.t', 'k.t'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m.88', 'https://about.me/m.88', 'm.88'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m-alo', 'https://about.me/m-alo', 'm-alo'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m-jantz', 'https://about.me/m-jantz', 'm-jantz'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'https://about.me/m-shoaib', 'https://about.me/m-shoaib', 'm-shoaib'),  # wayback-200; live 200 (unknown ids 404)
    ('about_me', 'http://about.me/m.a.banitamim', 'https://about.me/m.a.banitamim', 'm.a.banitamim'),  # wayback-200; live 200 (unknown ids 404)
    # GeeksforGeeks
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/123kapilpoonia123', 'https://www.geeksforgeeks.org/profile/123kapilpoonia123', '123kapilpoonia123'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/aishwarya.27', 'https://www.geeksforgeeks.org/profile/aishwarya.27', 'aishwarya.27'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/manuj-sankrit', 'https://www.geeksforgeeks.org/profile/manuj-sankrit', 'manuj-sankrit'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/__mahakaal__', 'https://www.geeksforgeeks.org/profile/__mahakaal__', '__mahakaal__'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/184025', 'https://www.geeksforgeeks.org/profile/184025', '184025'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/02DCE', 'https://www.geeksforgeeks.org/profile/02DCE', '02DCE'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/_Krish', 'https://www.geeksforgeeks.org/profile/_Krish', '_Krish'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/aark', 'https://www.geeksforgeeks.org/profile/aark', 'aark'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/adam', 'https://www.geeksforgeeks.org/profile/adam', 'adam'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/bkm3', 'https://www.geeksforgeeks.org/profile/bkm3', 'bkm3'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/Mr.L', 'https://www.geeksforgeeks.org/profile/Mr.L', 'Mr.L'),  # wayback-200; live 200
    ('geeksforgeeks', 'https://www.geeksforgeeks.org/profile/KJoy', 'https://www.geeksforgeeks.org/profile/KJoy', 'KJoy'),  # wayback-200; live 200
    # HackerOne
    ('hackerone', 'https://hackerone.com/m-a-v-e-r-i-c-k', 'https://hackerone.com/m-a-v-e-r-i-c-k', 'm-a-v-e-r-i-c-k'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m--j', 'https://hackerone.com/m--j', 'm--j'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m-m', 'https://hackerone.com/m-m', 'm-m'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m-s', 'https://hackerone.com/m-s', 'm-s'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m01', 'https://hackerone.com/m01', 'm01'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/k-1', 'https://hackerone.com/k-1', 'k-1'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/k00', 'https://hackerone.com/k00', 'k00'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/k0_', 'https://hackerone.com/k0_', 'k0_'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m-02', 'https://hackerone.com/m-02', 'm-02'),  # wayback-200; live 200 (unknown ids 404)
    ('hackerone', 'https://hackerone.com/m-75', 'https://hackerone.com/m-75', 'm-75'),  # wayback-200; live 200 (unknown ids 404)
    # Bugcrowd
    ('bugcrowd', 'https://bugcrowd.com/h/-', 'https://bugcrowd.com/h/-', '-'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/_shankyagarwal_', 'https://bugcrowd.com/h/_shankyagarwal_', '_shankyagarwal_'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/ads.txt', 'https://bugcrowd.com/h/ads.txt', 'ads.txt'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/-Z', 'https://bugcrowd.com/h/-Z', '-Z'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/0_czar', 'https://bugcrowd.com/h/0_czar', '0_czar'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/328', 'https://bugcrowd.com/h/328', '328'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/000jitender00', 'https://bugcrowd.com/h/000jitender00', '000jitender00'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/0Dr3f', 'https://bugcrowd.com/h/0Dr3f', '0Dr3f'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/9', 'https://bugcrowd.com/h/9', '9'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/2n', 'https://bugcrowd.com/h/2n', '2n'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/5rx', 'https://bugcrowd.com/h/5rx', '5rx'),  # wayback-200; live 200
    ('bugcrowd', 'https://bugcrowd.com/h/911', 'https://bugcrowd.com/h/911', '911'),  # wayback-200; live 200
    # Anaconda.org
    ('anaconda', 'https://anaconda.org/18', 'https://anaconda.org/18', '18'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/m-labs', 'https://anaconda.org/m-labs', 'm-labs'),  # wayback-200; live 200
    ('anaconda', 'http://anaconda.org/s_tbe', 'https://anaconda.org/s_tbe', 's_tbe'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/63', 'https://anaconda.org/63', '63'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/0x1997', 'https://anaconda.org/0x1997', '0x1997'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/s390x', 'https://anaconda.org/s390x', 's390x'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/kaija', 'https://anaconda.org/kaija', 'kaija'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/3dhubs', 'https://anaconda.org/3dhubs', '3dhubs'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/maddin', 'https://anaconda.org/maddin', 'maddin'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/maceo57', 'https://anaconda.org/maceo57', 'maceo57'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/s-ameli', 'https://anaconda.org/s-ameli', 's-ameli'),  # wayback-200; live 200
    ('anaconda', 'https://anaconda.org/saedrna', 'https://anaconda.org/saedrna', 'saedrna'),  # wayback-200; live 200
]


@pytest.mark.parametrize("platform,url,sanitized,bare_id", REAL_HANDLES)
def test_real_handle_url(sl, platform, url, sanitized, bare_id):
    assert sl.detect_platform(url) == platform
    assert sl.is_valid(platform, url)
    assert sl.sanitize(platform, url) == sanitized
    assert sl.sanitize(platform, sanitized) == sanitized


@pytest.mark.parametrize("platform,url,sanitized,bare_id", [r for r in REAL_HANDLES if r[3] is not None])
def test_real_handle_bare_id(sl, platform, url, sanitized, bare_id):
    assert sl.detect_platform(bare_id) is None
    assert sl.is_valid(platform, bare_id)
    assert sl.sanitize(platform, bare_id) == sanitized
