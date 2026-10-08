import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QComboBox,
    QTextEdit,
    QListWidget,
    QFrame,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


# ============================================================
# 공통 스타일
# ============================================================

APP_STYLE = """
    QWidget {
        background-color: #F5F7FA;
        color: #202124;
        font-family: "Malgun Gothic";
    }

    QLabel {
        background-color: transparent;
    }

    QFrame#card {
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
    }

    QLabel#title {
        color: #202124;
        font-size: 24px;
        font-weight: bold;
    }

    QLabel#subtitle {
        color: #7A7F87;
        font-size: 13px;
    }

    QLabel#sectionTitle {
        color: #202124;
        font-size: 16px;
        font-weight: bold;
    }

    QLabel#label {
        color: #454A52;
        font-size: 13px;
        font-weight: bold;
    }

    QPushButton#primaryButton {
        background-color: #333333;
        color: white;
        border: none;
        border-radius: 9px;
        padding: 12px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton#primaryButton:hover {
        background-color: #222222;
    }

    QPushButton#blueButton {
        background-color: #1976D2;
        color: white;
        border: none;
        border-radius: 9px;
        padding: 12px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton#blueButton:hover {
        background-color: #1565C0;
    }

    QPushButton#menuButton {
        background-color: white;
        color: #202124;
        border: 1px solid #E1E4E8;
        border-radius: 12px;
        padding: 16px;
        font-size: 15px;
        text-align: left;
    }

    QPushButton#menuButton:hover {
        background-color: #F8FAFC;
        border: 1px solid #B8C0CA;
    }

    QPushButton#subButton {
        background-color: transparent;
        color: #6B7078;
        border: none;
        font-size: 13px;
        padding: 6px;
    }

    QPushButton#subButton:hover {
        color: #1976D2;
    }

    QPushButton#backButton {
        background-color: transparent;
        color: #6B7078;
        border: none;
        font-size: 13px;
        padding: 6px;
    }

    QPushButton#backButton:hover {
        color: #202124;
    }

    QLineEdit {
        background-color: white;
        color: #202124;
        border: 1px solid #D9DDE3;
        border-radius: 9px;
        padding: 11px;
        font-size: 14px;
    }

    QLineEdit:focus {
        border: 2px solid #1976D2;
    }

    QComboBox {
        background-color: white;
        color: #202124;
        border: 1px solid #D9DDE3;
        border-radius: 9px;
        padding: 10px;
        font-size: 14px;
    }

    QComboBox:focus {
        border: 1px solid #1976D2;
    }

    QTextEdit {
        background-color: white;
        color: #202124;
        border: 1px solid #D9DDE3;
        border-radius: 9px;
        padding: 10px;
        font-size: 14px;
    }

    QTextEdit:focus {
        border: 1px solid #1976D2;
    }

    QPushButton#photoButton {
        background-color: #F8F9FB;
        color: #555B64;
        border: 1px dashed #C8CDD4;
        border-radius: 9px;
        padding: 10px;
        font-size: 13px;
    }

    QPushButton#photoButton:hover {
        background-color: #F1F5F9;
        border: 1px dashed #9CA3AF;
    }

    QLabel#value {
        background-color: #F8F9FB;
        color: #4B5058;
        border: 1px solid #E3E6EA;
        border-radius: 9px;
        padding: 11px;
        font-size: 14px;
    }

    QListWidget {
        background-color: white;
        border: 1px solid #E1E4E8;
        border-radius: 12px;
        padding: 5px;
        font-size: 14px;
    }

    QListWidget::item {
        padding: 17px;
        border-bottom: 1px solid #EEEEEE;
    }

    QListWidget::item:hover {
        background-color: #F8FAFC;
    }

    QListWidget::item:selected {
        background-color: #EEF5FC;
        color: #202124;
    }
"""


# ============================================================
# 로그인
# ============================================================

def login():

    student_id = id_input.text()
    password = password_input.text()

    if student_id == "" or password == "":
        QMessageBox.warning(
            window,
            "로그인",
            "학번과 비밀번호를 입력해주세요."
        )
    else:
        show_main_window()


# ============================================================
# 학생 메인 화면
# ============================================================

def show_main_window():

    window.hide()

    global main_window

    main_window = QWidget()
    main_window.setWindowTitle("기숙사 시설 관리 시스템")
    main_window.resize(520, 650)
    main_window.setStyleSheet(APP_STYLE)

    layout = QVBoxLayout()
    layout.setContentsMargins(35, 35, 35, 30)
    layout.setSpacing(15)

    # 상단
    header = QFrame()
    header.setObjectName("card")

    header_layout = QVBoxLayout()
    header_layout.setContentsMargins(25, 22, 25, 22)
    header_layout.setSpacing(5)

    title = QLabel("기숙사 시설 관리 시스템")
    title.setObjectName("title")

    student_label = QLabel(
        f"{id_input.text()}님, 안녕하세요."
    )
    student_label.setObjectName("subtitle")

    header_layout.addWidget(title)
    header_layout.addWidget(student_label)

    header.setLayout(header_layout)

    layout.addWidget(header)

    # 메뉴
    menu_title = QLabel("무엇을 도와드릴까요?")
    menu_title.setObjectName("sectionTitle")

    layout.addWidget(menu_title)

    # 민원 접수
    report_button = QPushButton(
        "📝  민원 접수\n"
        "      시설 문제나 생활 불편사항을 등록합니다."
    )

    report_button.setObjectName("menuButton")
    report_button.setFixedHeight(75)
    report_button.clicked.connect(show_report_window)

    # 내 신고 내역
    history_button = QPushButton(
        "📋  내 신고 내역\n"
        "      등록한 신고의 처리 상태를 확인합니다."
    )

    history_button.setObjectName("menuButton")
    history_button.setFixedHeight(75)
    history_button.clicked.connect(show_history_window)

    # 내 정보
    info_button = QPushButton(
        "👤  내 정보\n"
        "      학생 계정 정보를 확인합니다."
    )

    info_button.setObjectName("menuButton")
    info_button.setFixedHeight(75)
    info_button.clicked.connect(show_info_window)

    layout.addWidget(report_button)
    layout.addWidget(history_button)
    layout.addWidget(info_button)

    layout.addStretch()

    bottom_label = QLabel(
        "기숙사 생활 중 불편한 사항을 편리하게 신고하세요."
    )

    bottom_label.setObjectName("subtitle")
    bottom_label.setAlignment(Qt.AlignCenter)

    layout.addWidget(bottom_label)

    main_window.setLayout(layout)
    main_window.show()


# ============================================================
# 민원 접수 화면
# ============================================================

def show_report_window():

    main_window.hide()

    global report_window
    global problem_combo
    global location_combo
    global floor_combo
    global room_combo
    global floor_label
    global room_label
    global content_input

    report_window = QWidget()
    report_window.setWindowTitle("민원 접수")
    report_window.resize(520, 720)
    report_window.setStyleSheet(APP_STYLE)

    layout = QVBoxLayout()
    layout.setContentsMargins(35, 30, 35, 25)
    layout.setSpacing(10)

    # 제목
    title = QLabel("민원 접수")
    title.setObjectName("title")
    title.setAlignment(Qt.AlignCenter)

    subtitle = QLabel(
        "시설 문제 또는 생활 불편사항을 등록해주세요."
    )
    subtitle.setObjectName("subtitle")
    subtitle.setAlignment(Qt.AlignCenter)

    layout.addWidget(title)
    layout.addWidget(subtitle)

    layout.addSpacing(10)

    # --------------------------------------------------------
    # 민원 유형
    # --------------------------------------------------------

    type_card = QFrame()
    type_card.setObjectName("card")

    type_layout = QVBoxLayout()
    type_layout.setContentsMargins(18, 16, 18, 16)
    type_layout.setSpacing(7)

    type_label = QLabel("민원 유형")
    type_label.setObjectName("label")

    type_combo = QComboBox()

    type_combo.addItems([
        "시설 신고",
        "생활 불편"
    ])

    type_layout.addWidget(type_label)
    type_layout.addWidget(type_combo)

    type_card.setLayout(type_layout)

    layout.addWidget(type_card)

    # --------------------------------------------------------
    # 문제 유형
    # --------------------------------------------------------

    problem_card = QFrame()
    problem_card.setObjectName("card")

    problem_layout = QVBoxLayout()
    problem_layout.setContentsMargins(18, 16, 18, 16)
    problem_layout.setSpacing(7)

    problem_label = QLabel("문제 유형")
    problem_label.setObjectName("label")

    problem_combo = QComboBox()

    facility_types = [
        "전기·조명",
        "냉난방",
        "수도",
        "도어락",
        "기타"
    ]

    living_types = [
        "인터넷(WIFI)",
        "카드키 오류",
        "소음",
        "위생",
        "공사",
        "기타 생활 불편"
    ]

    problem_combo.addItems(facility_types)

    type_combo.currentIndexChanged.connect(
        lambda index: update_problem_types(
            type_combo,
            facility_types,
            living_types
        )
    )

    problem_layout.addWidget(problem_label)
    problem_layout.addWidget(problem_combo)

    problem_card.setLayout(problem_layout)

    layout.addWidget(problem_card)

    # --------------------------------------------------------
    # 발생 위치
    # --------------------------------------------------------

    location_card = QFrame()
    location_card.setObjectName("card")

    location_layout = QVBoxLayout()
    location_layout.setContentsMargins(18, 16, 18, 16)
    location_layout.setSpacing(7)

    location_label = QLabel("발생 위치")
    location_label.setObjectName("label")

    location_combo = QComboBox()

    location_combo.addItems([
        "기숙사 방(여)",
        "기숙사 방(남)",
        "휴게실",
        "세탁실",
        "복도",
        "기타 시설"
    ])

    location_layout.addWidget(location_label)
    location_layout.addWidget(location_combo)

    # 층 / 호수
    floor_label = QLabel("층")
    floor_label.setObjectName("label")

    floor_combo = QComboBox()

    floor_combo.addItems([
        "층 선택",
        "4층",
        "5층",
        "6층",
        "7층",
        "8층",
        "9층",
        "10층"
    ])

    room_label = QLabel("호수")
    room_label.setObjectName("label")

    room_combo = QComboBox()
    room_combo.addItem("호수 선택")

    floor_room_layout = QHBoxLayout()
    floor_room_layout.setSpacing(8)

    floor_room_layout.addWidget(floor_label)
    floor_room_layout.addWidget(floor_combo)

    floor_room_layout.addSpacing(10)

    floor_room_layout.addWidget(room_label)
    floor_room_layout.addWidget(room_combo)

    location_layout.addLayout(floor_room_layout)

    location_card.setLayout(location_layout)

    layout.addWidget(location_card)

    floor_combo.currentIndexChanged.connect(
        lambda index: update_room_list(
            floor_combo,
            room_combo
        )
    )

    location_combo.currentIndexChanged.connect(
        lambda index: update_location_fields(location_combo)
    )

    # --------------------------------------------------------
    # 상세 내용
    # --------------------------------------------------------

    content_card = QFrame()
    content_card.setObjectName("card")

    content_layout = QVBoxLayout()
    content_layout.setContentsMargins(18, 16, 18, 16)
    content_layout.setSpacing(7)

    content_label = QLabel("상세 내용")
    content_label.setObjectName("label")

    content_input = QTextEdit()

    content_input.setPlaceholderText(
        "문제를 자세히 입력해주세요."
    )

    content_input.setFixedHeight(100)

    content_layout.addWidget(content_label)
    content_layout.addWidget(content_input)

    content_card.setLayout(content_layout)

    layout.addWidget(content_card)

    # 사진 첨부
    photo_button = QPushButton(
        "📷  사진 첨부"
    )

    photo_button.setObjectName("photoButton")
    photo_button.setFixedHeight(42)

    layout.addWidget(photo_button)

    # 신고 등록
    register_button = QPushButton(
        "신고 등록"
    )

    register_button.setObjectName("blueButton")
    register_button.setFixedHeight(46)

    register_button.clicked.connect(register_report)

    layout.addWidget(register_button)

    # 이전
    back_button = QPushButton(
        "← 이전"
    )

    back_button.setObjectName("backButton")

    back_button.clicked.connect(
        back_to_main_from_report
    )

    layout.addWidget(
        back_button,
        alignment=Qt.AlignCenter
    )

    report_window.setLayout(layout)

    update_location_fields(location_combo)

    report_window.show()


# ============================================================
# 문제 유형 변경
# ============================================================

def update_problem_types(
    type_combo,
    facility_types,
    living_types
):

    problem_combo.clear()

    if type_combo.currentText() == "시설 신고":
        problem_combo.addItems(facility_types)
    else:
        problem_combo.addItems(living_types)


# ============================================================
# 발생 위치 변경
# ============================================================

def update_location_fields(location_combo):

    if location_combo.currentText() in [
        "기숙사 방(여)",
        "기숙사 방(남)"
    ]:

        floor_label.show()
        floor_combo.show()

        room_label.show()
        room_combo.show()

    else:

        floor_label.hide()
        floor_combo.hide()

        room_label.hide()
        room_combo.hide()


# ============================================================
# 층 선택 → 호수 목록
# ============================================================

def update_room_list(
    floor_combo,
    room_combo
):

    room_combo.clear()

    floor = floor_combo.currentText()

    if floor == "층 선택":

        room_combo.addItem("호수 선택")
        return

    floor_number = int(
        floor.replace("층", "")
    )

    room_numbers = [
        f"{floor_number}01호",
        f"{floor_number}02호",
        f"{floor_number}03호",
        f"{floor_number}04호",
        f"{floor_number}05호",
        f"{floor_number}06호",
        f"{floor_number}07호",
        f"{floor_number}08호",
        f"{floor_number}09호",
        f"{floor_number}10호",
        f"{floor_number}11호",
        f"{floor_number}12호",
        f"{floor_number}13호",
        f"{floor_number}14호",
        f"{floor_number}15호",
        f"{floor_number}16호",
        f"{floor_number}17호",
        f"{floor_number}18호",
        f"{floor_number}19호",
        f"{floor_number}20호",
        f"{floor_number}21호",
        f"{floor_number}22호",
        f"{floor_number}23호",
        f"{floor_number}24호",
        f"{floor_number}25호",
        f"{floor_number}26호",
        f"{floor_number}27호",
        f"{floor_number}28호",
        f"{floor_number}29호",
        f"{floor_number}30호",
        f"{floor_number}31호",
    ]

    room_combo.addItem("호수 선택")
    room_combo.addItems(room_numbers)


# ============================================================
# 신고 등록
# 현재는 UI 테스트용
# ============================================================

def register_report():

    location = location_combo.currentText()
    content = content_input.toPlainText().strip()

    if location in [
        "기숙사 방(여)",
        "기숙사 방(남)"
    ]:

        if floor_combo.currentText() == "층 선택":

            QMessageBox.warning(
                report_window,
                "신고 등록",
                "발생 층을 선택해주세요."
            )

            return

        if room_combo.currentText() == "호수 선택":

            QMessageBox.warning(
                report_window,
                "신고 등록",
                "호수를 선택해주세요."
            )

            return

    if content == "":

        QMessageBox.warning(
            report_window,
            "신고 등록",
            "상세 내용을 입력해주세요."
        )

        return

    QMessageBox.information(
        report_window,
        "신고 등록",
        "신고가 등록되었습니다."
    )


# ============================================================
# 민원 접수 → 메인
# ============================================================

def back_to_main_from_report():

    report_window.close()
    main_window.show()


# ============================================================
# 내 신고 내역
# 기존 UI 그대로
# ============================================================

def show_history_window():

    main_window.hide()

    global history_window

    history_window = QWidget()
    history_window.setWindowTitle("내 신고 내역")
    history_window.resize(520, 650)
    history_window.setStyleSheet(APP_STYLE)

    layout = QVBoxLayout()

    layout.setContentsMargins(
        35,
        35,
        35,
        30
    )

    layout.setSpacing(12)

    # 제목 카드
    header = QFrame()
    header.setObjectName("card")

    header_layout = QVBoxLayout()

    header_layout.setContentsMargins(
        22,
        20,
        22,
        20
    )

    title = QLabel("내 신고 내역")
    title.setObjectName("title")

    subtitle = QLabel(
        "등록한 신고의 처리 상태를 확인할 수 있습니다."
    )

    subtitle.setObjectName("subtitle")

    header_layout.addWidget(title)
    header_layout.addWidget(subtitle)

    header.setLayout(header_layout)

    layout.addWidget(header)

    # 신고 목록
    history_list = QListWidget()

    history_list.addItem(
        "🏢 전기·조명\n"
        "처리 상태: 처리 중"
    )

    history_list.addItem(
        "📶 와이파이·인터넷\n"
        "처리 상태: 처리 완료"
    )

    history_list.addItem(
        "🔊 소음\n"
        "처리 상태: 접수 완료"
    )

    layout.addWidget(history_list)

    layout.addStretch()

    # 메인으로
    back_button = QPushButton(
        "← 메인 화면으로"
    )

    back_button.setObjectName(
        "backButton"
    )

    back_button.clicked.connect(
        back_to_main_from_history
    )

    layout.addWidget(
        back_button,
        alignment=Qt.AlignCenter
    )

    history_window.setLayout(layout)

    history_window.show()


# ============================================================
# 신고 내역 → 메인
# ============================================================

def back_to_main_from_history():

    history_window.close()
    main_window.show()


# ============================================================
# 내 정보
# ============================================================

def show_info_window():

    main_window.hide()

    global info_window

    info_window = QWidget()
    info_window.setWindowTitle("내 정보")
    info_window.resize(520, 650)
    info_window.setStyleSheet(APP_STYLE)

    layout = QVBoxLayout()

    layout.setContentsMargins(
        35,
        35,
        35,
        30
    )

    layout.setSpacing(12)

    # 프로필 카드
    profile_card = QFrame()
    profile_card.setObjectName("card")

    profile_layout = QVBoxLayout()

    profile_layout.setContentsMargins(
        25,
        25,
        25,
        25
    )

    profile_layout.setSpacing(7)

    profile_icon = QLabel("👤")

    profile_icon.setAlignment(
        Qt.AlignCenter
    )

    profile_icon.setFont(
        QFont("Arial", 38)
    )

    title = QLabel("내 정보")
    title.setObjectName("title")
    title.setAlignment(Qt.AlignCenter)

    subtitle = QLabel(
        "학생 계정 정보를 확인할 수 있습니다."
    )

    subtitle.setObjectName("subtitle")
    subtitle.setAlignment(Qt.AlignCenter)

    profile_layout.addWidget(profile_icon)
    profile_layout.addWidget(title)
    profile_layout.addWidget(subtitle)

    profile_card.setLayout(profile_layout)

    layout.addWidget(profile_card)

    # 계정 정보
    info_card = QFrame()
    info_card.setObjectName("card")

    info_layout = QVBoxLayout()

    info_layout.setContentsMargins(
        22,
        20,
        22,
        20
    )

    info_layout.setSpacing(7)

    account_title = QLabel("계정 정보")
    account_title.setObjectName("sectionTitle")

    info_layout.addWidget(account_title)

    info_layout.addSpacing(5)

    # 학번
    id_label = QLabel("학번")
    id_label.setObjectName("label")

    id_value = QLabel(
        id_input.text()
    )

    id_value.setObjectName("value")

    info_layout.addWidget(id_label)
    info_layout.addWidget(id_value)

    info_layout.addSpacing(8)

    # 이름
    name_label = QLabel("이름")
    name_label.setObjectName("label")

    name_value = QLabel(
        "홍길동"
    )

    name_value.setObjectName("value")

    info_layout.addWidget(name_label)
    info_layout.addWidget(name_value)

    info_layout.addSpacing(8)

    # 이메일
    email_label = QLabel("이메일")
    email_label.setObjectName("label")

    email_value = QLabel(
        "example@email.com"
    )

    email_value.setObjectName("value")

    info_layout.addWidget(email_label)
    info_layout.addWidget(email_value)

    info_card.setLayout(info_layout)

    layout.addWidget(info_card)

    # 계정 관리
    account_card = QFrame()
    account_card.setObjectName("card")

    account_layout = QVBoxLayout()

    account_layout.setContentsMargins(
        22,
        18,
        22,
        18
    )

    account_title = QLabel("계정 관리")
    account_title.setObjectName("sectionTitle")

    account_layout.addWidget(account_title)

    password_button = QPushButton(
        "🔑  비밀번호 변경"
    )

    password_button.setObjectName(
        "menuButton"
    )

    password_button.setFixedHeight(50)

    account_layout.addWidget(password_button)

    account_card.setLayout(account_layout)

    layout.addWidget(account_card)

    layout.addStretch()

    # 메인으로
    back_button = QPushButton(
        "← 메인 화면으로"
    )

    back_button.setObjectName(
        "backButton"
    )

    back_button.clicked.connect(
        back_to_main_from_info
    )

    layout.addWidget(
        back_button,
        alignment=Qt.AlignCenter
    )

    info_window.setLayout(layout)

    info_window.show()


# ============================================================
# 내 정보 → 메인
# ============================================================

def back_to_main_from_info():

    info_window.close()
    main_window.show()


# ============================================================
# 로그인 화면
# ============================================================

def create_login_window():

    global window
    global id_input
    global password_input

    window = QWidget()

    window.setWindowTitle(
        "기숙사 시설 관리 시스템"
    )

    window.resize(520, 650)

    window.setStyleSheet(
        APP_STYLE
    )

    layout = QVBoxLayout()

    layout.setContentsMargins(
        65,
        55,
        65,
        45
    )

    layout.setSpacing(12)

    layout.addStretch()

    # 로그인 카드
    login_card = QFrame()
    login_card.setObjectName(
        "card"
    )

    card_layout = QVBoxLayout()

    card_layout.setContentsMargins(
        35,
        35,
        35,
        30
    )

    card_layout.setSpacing(12)

    # 건물 아이콘
    building = QLabel("🏢")

    building.setAlignment(
        Qt.AlignCenter
    )

    building.setFont(
        QFont("Arial", 42)
    )

    # 시스템 제목
    system_title = QLabel(
        "기숙사 시설 관리 시스템"
    )

    system_title.setObjectName(
        "title"
    )

    system_title.setAlignment(
        Qt.AlignCenter
    )

    # 부제목
    subtitle = QLabel(
        "학생 로그인"
    )

    subtitle.setObjectName(
        "subtitle"
    )

    subtitle.setAlignment(
        Qt.AlignCenter
    )

    card_layout.addWidget(building)
    card_layout.addWidget(system_title)
    card_layout.addWidget(subtitle)

    card_layout.addSpacing(15)

    # 학번
    id_label = QLabel("학번")
    id_label.setObjectName("label")

    id_input = QLineEdit()

    id_input.setPlaceholderText(
        "학번을 입력하세요"
    )

    id_input.setFixedHeight(44)

    card_layout.addWidget(id_label)
    card_layout.addWidget(id_input)

    # 비밀번호
    password_label = QLabel("비밀번호")
    password_label.setObjectName("label")

    password_input = QLineEdit()

    password_input.setPlaceholderText(
        "비밀번호를 입력하세요"
    )

    password_input.setEchoMode(
        QLineEdit.Password
    )

    password_input.setFixedHeight(44)

    card_layout.addWidget(password_label)
    card_layout.addWidget(password_input)

    card_layout.addSpacing(5)

    # 로그인
    login_button = QPushButton(
        "로그인"
    )

    login_button.setObjectName(
        "blueButton"
    )

    login_button.setFixedHeight(46)

    login_button.clicked.connect(
        login
    )

    card_layout.addWidget(login_button)

    card_layout.addSpacing(2)

    # 회원가입 / 비밀번호 찾기
    bottom_layout = QHBoxLayout()

    signup_button = QPushButton(
        "회원가입"
    )

    signup_button.setObjectName(
        "subButton"
    )

    find_button = QPushButton(
        "비밀번호 찾기"
    )

    find_button.setObjectName(
        "subButton"
    )

    bottom_layout.addStretch()

    bottom_layout.addWidget(
        signup_button
    )

    bottom_layout.addWidget(
        find_button
    )

    bottom_layout.addStretch()

    card_layout.addLayout(
        bottom_layout
    )

    login_card.setLayout(
        card_layout
    )

    layout.addWidget(
        login_card
    )

    layout.addStretch()

    # 하단 안내
    footer = QLabel(
        "Dormitory Facility Management System"
    )

    footer.setObjectName(
        "subtitle"
    )

    footer.setAlignment(
        Qt.AlignCenter
    )

    layout.addWidget(footer)

    window.setLayout(layout)

    return window


# ============================================================
# 프로그램 실행
# ============================================================

def main():

    app = QApplication(
        sys.argv
    )

    login_window = create_login_window()

    login_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()