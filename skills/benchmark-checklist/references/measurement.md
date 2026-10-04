# 측정 주장 검토

먼저 실제 보고할 주장, 측정 script가 시간을 재는 범위·세는 일·빠뜨리는 일을 읽는다. OS에 맞는 기존 도구로 load·core 수·다른 작업을 확인한다. 다른 작업을 임의 종료하지 않는다. 노이즈가 있으면 A/B를 교차 측정하고 환경을 보고한다.

1. 왜 두 배가 아닌가. 보고용 측정과 별도의 profiling run에서 limiter를 찾는다. profiler 오버헤드가 측정값에 섞이지 않게 한다. load generator가 먼저 포화되면 그것을 측정했다고 구분한다. 개선이 숫자를 못 바꾸면 limiter를 확인한 뒤 판단한다.
2. 동일하게 튜닝했는가. production/release mode·flag·버전·데이터·batch/transaction·pool·실제 warm/cold cache 조건을 맞춘다. 한 쪽의 debug/default/누락 index가 병목이면 설정 비교다. option 선택을 위한 winner 판정은 튜닝 후에만 하며 못 하면 미확인이다.
3. 물리적·비율 한계를 넘는가. bytes/sec를 disk/network bound, operations×cost를 core와 비교한다. 전체 시간의 10% 부분을 없애도 최대 속도 증가가 약 11%라는 상한을 확인한다. 한계를 넘는 숫자는 cache·no-op·누락·오류를 의심한다.
4. 오류가 없는가. 실패·non-success·retry·timeout과 실제 결과의 정확성을 센다. reject는 빠르고 retry는 느릴 수 있다. 오류를 세지 않는 harness는 필요한 scope에서 고친다.
5. 반복되는가. 비교 판정은 각 측면 최소 5회 A/B 교차 측정하고 median·range를 보고한다. gap이 run-to-run variation보다 작으면 '측정 가능한 차이 없음'이다. 가까운 결과에는 기존 harness statistics나 알맞은 통계를 사용한다.
6. 사용자에게 중요한가. micro metric 옆에 실제 사용자 end-to-end 경로·현실적인 데이터/동시성을 측정한다. 전체의 1% helper를 개선해 전체가 그보다 크게 개선됐다고 주장하지 않는다.
7. 일이 실제로 일어났는가. timed region 안에서 request 도착·rows/bytes 처리·결과 사용·await·lazy iteration을 확인한다. 아무도 소비하지 않은 결과나 timeout을 실제 처리 완료로 세지 않는다.

사용자가 대략적인 1회 estimate만 요청하면 오류와 실제 처리 여부는 확인하고 1회임을 명시한다. option winner 결정은 이 예외에 해당하지 않는다.

판정은 빨라짐·느려짐·측정 가능한 차이 없음·미확인이다. 단위·run 수·range·limiter를 함께 보고한다. 차이를 주장하면서 limiter를 못 찾거나 한 쪽이 untuned이거나 오류/실제 처리 여부를 못 확인하면 미확인이다. PR에는 주요 수치 하나와 최소 supporting 근거만 넣고 자세한 원시 결과는 개인 evidence에 둔다.
