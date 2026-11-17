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
    ('clawhub', 'https://clawhub.ai/404-lobster-detective.jpg', 'https://clawhub.ai/404-lobster-detective.jpg', '404-lobster-detective.jpg'),  # wayback-200; live 200 (unknown ids 404)
    ('clawhub', 'https://clawhub.ai/manifest.json', 'https://clawhub.ai/manifest.json', 'manifest.json'),  # wayback-200; live 200 (unknown ids 404)
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
