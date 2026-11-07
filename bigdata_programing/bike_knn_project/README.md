# 서울 공유자전거 KNN 실습

`bike_knn.ipynb`에서 CSV 처리, 등급 생성, 8:2 분할, Min-Max 정규화, 유클리드 거리, 이웃 선택, 다수결, 정확도 비교를 차례로 학습합니다. KNN은 파이썬으로 직접 구현했고 sklearn은 사용하지 않습니다. pandas는 데이터 처리, matplotlib은 그래프 출력에만 사용합니다.

## 실행 방법

VS Code에서 `bike_knn.ipynb`를 열고, 우측 상단 **커널 선택 → Python 환경**에서 이 폴더의 `.venv/Scripts/python.exe`를 선택한 뒤 **모두 실행**을 누르세요. 커널이 목록에 없으면 해당 인터프리터 경로를 직접 선택하세요. VS Code의 Python 및 Jupyter 확장이 필요합니다.

가상환경을 새로 설치하는 경우, 이 폴더에서 PowerShell로 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

실행하면 K=1, 3, 5, 7, 9의 정확도가 출력되고 그래프가 노트북에 표시됩니다. 그래프는 같은 폴더의 `knn_accuracy.png`에도 저장됩니다. 기본 난수 시드는 42입니다.

## 데이터와 분류 기준

- 원본: [UCI Seoul Bike Sharing Demand](https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand)
- 다운로드: [UCI 공식 ZIP](https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip)
- `SeoulBikeData.csv`는 ZIP에 들어 있는 원본 CSV입니다. 날짜나 영업 여부로 추가 필터링하지 않습니다.
- 입력: `Hour`, `Temperature(°C)`, `Humidity(%)`. 온도와 습도 열 이름은 코드에서 간단히 바꿉니다.
- 정답: 전체 유효 데이터의 `Rented Bike Count`를 1/3·2/3 분위수로 나눠 Low, Medium, High로 변환합니다. 경계값과 같은 대여량은 낮은 쪽 등급에 포함됩니다. 중복 대여량 때문에 등급별 행 수가 조금 다를 수 있습니다.
- 결측치와 숫자로 바꿀 수 없는 값이 포함된 행은 제외합니다.
- 정규화는 **학습 데이터의 최솟값·최댓값만** 사용합니다. 테스트 데이터도 같은 기준으로 변환합니다.
- 다수결 동점은 최다 득표 등급 중 가장 가까운 이웃의 등급을 선택합니다. 거리도 같으면 고정된 학습 목록 순서를 따릅니다.

이 예제의 K 비교는 동일한 무작위 테스트셋에서 수행하는 실습 결과입니다. 새로운 데이터에 대한 최종 성능 평가나 미래 시점 예측을 평가하려면 별도의 검증/평가 설계가 필요합니다.
