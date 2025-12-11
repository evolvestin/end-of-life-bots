import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKENS = [token.strip() for token in os.getenv('TOKENS', '').split(',') if token.strip()]
dev_bot = Bot(token=os.getenv('DEV_TOKEN'))

ID_DEV = int(os.getenv('ID_DEV', 0))
ID_LOGS = int(os.getenv('ID_LOGS', 0))
ID_MEDIA = int(os.getenv('ID_MEDIA', 0))
ID_FORWARD = int(os.getenv('ID_FORWARD', 0))

IGNORE_ERRORS_PATTERN = '|'.join(
    [
        'Backend Error',
        'Read timed out.',
        'Message_id_invalid',
        'Connection aborted',
        'ServerDisconnectedError',
        'Connection reset by peer',
        'is currently unavailable.',
        'returned "Internal Error"',
        'Message to forward not found',
        'Message can&#39;t be forwarded',
        'Failed to establish a new connection',
        'The (read|write) operation timed out',
        'EOF occurred in violation of protocol',
    ]
)

ALLOWED_UPDATES = [
    'callback_query',
    'channel_post',
    'chat_member',
    'edited_channel_post',
    'edited_message',
    'message',
    'my_chat_member',
]

END_OF_LIFE_MESSAGES = {
    # Russian
    'ru': (
        '<b>Уведомление о прекращении работы сервиса</b>\n\n'
        'Сообщаем, что работа и техническая поддержка данного программного обеспечения (бота) '
        'полностью и окончательно прекращены.\n'
        'Решение о выводе системы из эксплуатации принято из-за отсутствия реальной необходимости '
        'в её функционале и отсутствия оснований для дальнейшего расходования ресурсов на её обслуживание.\n'
        'Все автоматические процессы остановлены, базы данных архивированы либо удалены, '
        'а серверные мощности перераспределены. '
        'Поступающие запросы, команды и сообщения отныне не обрабатываются и не получают ответа.\n'
        'Для запросов о доступе к архивным данным или о причинах прекращения работы вы можете '
        f'направить официальное обращение администратору проекта: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # English
    'en': (
        '<b>End of Service Notification</b>\n\n'
        'Please be advised that the operation and technical support for this software (bot) '
        'have been fully and permanently discontinued.\n'
        'The decision to decommission the system was reached due to the lack of actual demand '
        'for its functionality and the absence of justification for further resource allocation '
        'towards its administration.\n'
        'Effective immediately, all automated processes have been halted, databases have been archived or deleted, '
        'and server capacity has been reallocated. '
        'Incoming requests, commands, and messages are no longer being processed and will not be addressed.\n'
        'For any inquiries regarding archived data or the rationale behind the service termination, '
        f'you may submit a formal request to the project administrator: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Spanish
    'es': (
        '<b>Notificación de Cese de Servicio</b>\n\n'
        'Por la presente se comunica que la operación y el soporte técnico de este software (bot) '
        'han sido definitiva y totalmente suspendidos.\n'
        'La decisión de retirar el sistema se debe a la falta de demanda efectiva de su funcionalidad '
        'y a la ausencia de justificación para continuar asignando recursos a su administración.\n'
        'A partir de este momento, todos los procesos automatizados han sido detenidos, las bases de datos archivadas o eliminadas, '
        'y la capacidad del servidor reasignada. '
        'Las solicitudes, comandos y mensajes entrantes ya no se procesan ni serán atendidos.\n'
        'Para cualquier consulta relacionada con datos archivados o los motivos del cese de operaciones, '
        f'puede enviar una solicitud formal al administrador del proyecto: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Chinese (Simplified)
    'zh': (
        '<b>服务终止通知</b>\n\n'
        '特此通知，本软件（机器人）的运营和技术支持已完全、永久终止。\n'
        '由于该系统的功能需求不足，且继续投入管理资源已无合理依据，决定正式将其退役。\n'
        '目前，所有自动化流程已停止，数据库已归档或删除，服务器资源已重新分配。'
        '今后传入的请求、指令和消息将不再被处理或回复。\n'
        '如需查询存档数据或了解终止服务的原因，'
        f'您可向项目管理员提交正式请求：{os.getenv("LINK_TO_ADMIN")}。'
    ),
    # Portuguese
    'pt': (
        '<b>Aviso de Encerramento de Serviço</b>\n\n'
        'Informamos que a operação e o suporte técnico deste software (bot) '
        'foram totalmente e permanentemente descontinuados.\n'
        'A decisão de desativar o sistema foi tomada em razão da baixa demanda real '
        'por suas funcionalidades e da falta de justificativa para continuar destinando recursos '
        'à sua administração.\n'
        'Com efeito imediato, todos os processos automatizados foram interrompidos, os bancos de dados arquivados ou excluídos, '
        'e a capacidade do servidor foi realocada. '
        'Solicitações, comandos e mensagens recebidos não serão mais processados nem respondidos.\n'
        'Para dúvidas relacionadas a dados arquivados ou aos motivos do encerramento do serviço, '
        f'você pode enviar uma solicitação formal ao administrador do projeto: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # French
    'fr': (
        '<b>Avis de cessation de service</b>\n\n'
        'Nous vous informons que l’exploitation et le support technique de ce logiciel (bot) '
        'ont été définitivement et entièrement arrêtés.\n'
        'La décision de mettre fin au service a été prise en raison de l’absence de demande réelle '
        'pour ses fonctionnalités et du manque de justification quant à la poursuite de l’allocation de ressources '
        'à son administration.\n'
        'Désormais, tous les processus automatisés sont arrêtés, les bases de données ont été archivées ou supprimées, '
        'et les capacités des serveurs ont été réaffectées. '
        'Les requêtes, commandes et messages entrants ne sont plus traités et ne recevront aucune réponse.\n'
        'Pour toute question concernant les données archivées ou les raisons de cet arrêt, '
        f'vous pouvez adresser une demande officielle à l’administrateur du projet : {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # German
    'de': (
        '<b>Benachrichtigung über die Einstellung des Dienstes</b>\n\n'
        'Hiermit teilen wir Ihnen mit, dass der Betrieb und der technische Support für diese Software (Bot) '
        'vollständig und endgültig eingestellt wurden.\n'
        'Die Entscheidung zur Außerbetriebnahme des Systems wurde aufgrund mangelnder tatsächlicher Nachfrage '
        'nach dessen Funktionalität und fehlender Rechtfertigung für die weitere Zuweisung von Ressourcen '
        'für die Verwaltung getroffen.\n'
        'Ab sofort sind alle automatisierten Prozesse gestoppt, Datenbanken archiviert oder gelöscht '
        'und Serverkapazitäten neu zugewiesen. '
        'Eingehende Anfragen, Befehle und Nachrichten werden nicht mehr verarbeitet und bleiben unbeantwortet.\n'
        'Für Anfragen bezüglich archivierter Daten oder der Gründe für die Einstellung des Dienstes '
        f'können Sie eine formelle Anfrage an den Projektadministrator richten: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Arabic
    'ar': (
        '<b>إشعار إنهاء الخدمة</b>\n\n'
        'نود إعلامكم بأن تشغيل هذا البرنامج (البوت) ودعمه الفني قد تم إيقافهما بالكامل وبشكل نهائي.\n'
        'اتُّخذ قرار إيقاف النظام نتيجة لعدم وجود حاجة فعلية لوظائفه '
        'ولانتفاء الجدوى من الاستمرار في تخصيص الموارد لإدارته.\n'
        'اعتبارًا من الآن، تم إيقاف جميع العمليات المؤتمتة، وأرشفة قواعد البيانات أو حذفها، '
        'كما تمت إعادة توزيع موارد الخادم. '
        'لن تتم معالجة الطلبات أو الأوامر أو الرسائل الواردة بعد الآن، ولن يُقدَّم أي رد عليها.\n'
        'لأي استفسارات تتعلق بالبيانات المؤرشفة أو أسباب إنهاء الخدمة، '
        f'يمكنكم تقديم طلب رسمي إلى مسؤول المشروع: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Indonesian
    'id': (
        '<b>Pemberitahuan Penghentian Layanan</b>\n\n'
        'Dengan ini kami informasikan bahwa operasi dan dukungan teknis untuk perangkat lunak (bot) ini '
        'telah dihentikan sepenuhnya dan secara permanen.\n'
        'Keputusan untuk menonaktifkan sistem diambil karena kurangnya permintaan aktual '
        'terhadap fungsionalitasnya dan tidak adanya pembenaran untuk alokasi sumber daya lebih lanjut '
        'demi administrasi sistem.\n'
        'Saat ini, semua proses otomatis telah dihentikan, basis data telah diarsipkan atau dihapus, '
        'dan kapasitas server telah dialokasikan kembali. '
        'Permintaan, perintah, dan pesan yang masuk tidak lagi diproses dan tidak akan ditanggapi.\n'
        'Untuk pertanyaan apa pun mengenai data yang diarsipkan atau alasan penghentian layanan, '
        f'Anda dapat mengajukan permintaan resmi kepada administrator proyek: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Japanese
    'ja': (
        '<b>サービス終了のお知らせ</b>\n\n'
        '本ソフトウェア（ボット）の運用および技術サポートは、完全かつ恒久的に終了いたしました。\n'
        '本システムを停止する決定は、機能に対する実質的な需要がなく、'
        '管理リソースを継続投入する正当性が認められなかったために行われたものです。\n'
        '現在、すべての自動化プロセスは停止され、データベースはアーカイブまたは削除され、'
        'サーバーリソースは再割り当て済みです。 '
        '今後、受信したリクエスト、コマンド、メッセージが処理されることはなく、対応もいたしません。\n'
        'アーカイブデータやサービス終了の理由に関するお問い合わせは、'
        f'プロジェクト管理者まで正式にご連絡ください：{os.getenv("LINK_TO_ADMIN")}。'
    ),
    # Turkish
    'tr': (
        '<b>Hizmet Sonlandırma Bildirimi</b>\n\n'
        'Bu yazılımın (botun) işletimi ve teknik desteğinin tamamen ve kalıcı olarak durdurulduğunu bildiririz.\n'
        'Sistemi devre dışı bırakma kararı, işlevselliğine yönelik fiili talep eksikliği '
        've yönetimi için daha fazla kaynak ayrılmasının gerekçelendirilememesi nedeniyle alınmıştır.\n'
        'Şu an itibarıyla tüm otomatik süreçler durdurulmuş, veritabanları arşivlenmiş veya silinmiş '
        've sunucu kapasitesi yeniden tahsis edilmiştir. '
        'Gelen istekler, komutlar ve mesajlar artık işlenmemektedir ve yanıtlanmayacaktır.\n'
        'Arşivlenmiş veriler veya hizmetin sonlandırılma gerekçesi ile ilgili her türlü sorunuz için '
        f'proje yöneticisine resmi bir talep iletebilirsiniz: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Italian
    'it': (
        '<b>Avviso di cessazione del servizio</b>\n\n'
        "Si comunica che l'operatività e il supporto tecnico per questo software (bot) "
        'sono stati definitivamente e completamente interrotti.\n'
        'La decisione di dismettere il sistema è stata presa a causa della mancanza di una domanda effettiva '
        "per le sue funzionalità e dell'assenza di giustificazioni per l'ulteriore allocazione di risorse "
        'per la sua amministrazione.\n'
        'Con effetto immediato, tutti i processi automatizzati sono stati arrestati, i database archiviati o cancellati '
        'e le capacità del server riassegnate. '
        'Le richieste, i comandi e i messaggi in arrivo non vengono più elaborati e non riceveranno risposta.\n'
        'Per eventuali richieste riguardanti i dati archiviati o le motivazioni della cessazione del servizio, '
        f"è possibile inviare una richiesta formale all'amministratore del progetto: {os.getenv('LINK_TO_ADMIN')}."
    ),
    # Hindi
    'hi': (
        '<b>सेवा समाप्ति की सूचना</b>\n\n'
        'आपको सूचित किया जाता है कि इस सॉफ़्टवेयर (बॉट) का संचालन और तकनीकी सहायता '
        'पूर्ण रूप से और स्थायी तौर पर बंद कर दी गई है।\n'
        'सिस्टम को सेवामुक्त करने का निर्णय इसकी कार्यक्षमता की वास्तविक मांग की कमी '
        'और इसके प्रशासन के लिए संसाधनों के आवंटन को जारी रखने के औचित्य के अभाव के कारण लिया गया है।\n'
        'तत्काल प्रभाव से, सभी स्वचालित प्रक्रियाओं को रोक दिया गया है, डेटाबेस को आर्काइव या हटा दिया गया है, '
        'और सर्वर क्षमता को पुनर्वितरित कर दिया गया है। '
        'आने वाले अनुरोधों, कमांड और संदेशों पर अब कोई कार्रवाई नहीं की जा रही है और न ही उनका उत्तर दिया जाएगा।\n'
        'आर्काइव किए गए डेटा या सेवा समाप्ति के कारणों के संबंध में किसी भी प्रश्न के लिए, '
        f'आप परियोजना प्रशासक को औपचारिक अनुरोध भेज सकते हैं: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Korean
    'ko': (
        '<b>서비스 종료 통지</b>\n\n'
        '본 소프트웨어(봇)의 운영 및 기술 지원이 영구적으로 완전히 중단되었음을 알려드립니다.\n'
        '시스템 운영 중단 결정은 기능에 대한 실질적인 수요 부족과 '
        '관리 리소스를 지속적으로 투입할 타당성이 결여됨에 따라 내려졌습니다.\n'
        '현재 모든 자동화 프로세스가 중단되었으며, 데이터베이스는 보관 또는 삭제되었고, '
        '서버 리소스는 재할당되었습니다. '
        '수신되는 요청, 명령어 및 메시지는 더 이상 처리되지 않으며 응답이 제공되지 않습니다.\n'
        '보관된 데이터나 서비스 종료 사유에 관한 문의 사항이 있는 경우, '
        f'프로젝트 관리자에게 공식 요청을 보내실 수 있습니다: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Polish
    'pl': (
        '<b>Powiadomienie o zakończeniu świadczenia usług</b>\n\n'
        'Niniejszym informujemy, że eksploatacja i wsparcie techniczne tego oprogramowania (bota) '
        'zostały całkowicie i trwale zakończone.\n'
        'Decyzja o wycofaniu systemu z eksploatacji została podjęta z powodu braku faktycznego zapotrzebowania '
        'na jego funkcjonalność oraz braku uzasadnienia dla dalszego alokowania zasobów na jego administrację.\n'
        'W trybie natychmiastowym wszystkie zautomatyzowane procesy zostały zatrzymane, bazy danych zarchiwizowane lub usunięte, '
        'a zasoby serwerowe zostały przydzielone do innych zadań. '
        'Przychodzące żądania, polecenia i wiadomości nie są już przetwarzane i pozostaną bez odpowiedzi.\n'
        'W przypadku pytań dotyczących zarchiwizowanych danych lub przyczyn zakończenia działalności, '
        f'mogą Państwo przesłać oficjalne zapytanie do administratora projektu: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Dutch
    'nl': (
        '<b>Kennisgeving van beëindiging van de dienstverlening</b>\n\n'
        'Hierbij informeren wij u dat de werking en technische ondersteuning van deze software (bot) '
        'volledig en permanent zijn stopgezet.\n'
        'Het besluit om het systeem buiten gebruik te stellen is genomen vanwege het gebrek aan daadwerkelijke vraag '
        'naar de functionaliteit en de afwezigheid van rechtvaardiging voor verdere toewijzing van middelen '
        'voor het beheer ervan.\n'
        'Met onmiddellijke ingang zijn alle geautomatiseerde processen gestopt, databases gearchiveerd of verwijderd '
        'en servercapaciteit opnieuw toegewezen. '
        "Binnenkomende verzoeken, commando's en berichten worden niet langer verwerkt en zullen niet worden beantwoord.\n"
        'Voor vragen over gearchiveerde gegevens of de redenen voor de beëindiging van de dienst, '
        f'kunt u een formeel verzoek indienen bij de projectbeheerder: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Vietnamese
    'vi': (
        '<b>Thông báo Ngừng Cung cấp Dịch vụ</b>\n\n'
        'Chúng tôi xin thông báo rằng việc vận hành và hỗ trợ kỹ thuật cho phần mềm (bot) này '
        'đã bị chấm dứt hoàn toàn và vĩnh viễn.\n'
        'Quyết định ngừng hoạt động hệ thống được đưa ra do thiếu nhu cầu thực tế đối với các chức năng của nó '
        'và không còn lý do chính đáng để tiếp tục phân bổ tài nguyên cho việc quản trị.\n'
        'Ngay lập tức, tất cả các quy trình tự động đã bị dừng, cơ sở dữ liệu đã được lưu trữ hoặc xóa bỏ, '
        'và tài nguyên máy chủ đã được phân bổ lại. '
        'Các yêu cầu, lệnh và tin nhắn gửi đến sẽ không còn được xử lý hay phản hồi.\n'
        'Đối với mọi thắc mắc liên quan đến dữ liệu lưu trữ hoặc lý do chấm dứt dịch vụ, '
        f'quý vị có thể gửi yêu cầu chính thức tới quản trị viên dự án: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Thai
    'th': (
        '<b>ประกาศยุติการให้บริการ</b>\n\n'
        'ขอแจ้งให้ทราบว่าการดำเนินงานและการสนับสนุนทางเทคนิคสำหรับซอฟต์แวร์ (บอท) นี้ '
        'ได้ยุติลงอย่างสมบูรณ์และถาวรแล้ว\n'
        'การตัดสินใจเลิกใช้งานระบบมีสาเหตุมาจากการขาดความต้องการในการใช้งานจริง '
        'และการจัดสรรทรัพยากรเพื่อการบริหารจัดการต่อไปนั้นไม่มีความจำเป็นอีกต่อไป\n'
        'ณ ปัจจุบัน กระบวนการอัตโนมัติทั้งหมดได้ถูกระงับ ฐานข้อมูลถูกจัดเก็บหรือลบออก '
        'และทรัพยากรเซิร์ฟเวอร์ได้รับการจัดสรรใหม่ '
        'คำร้องขอ คำสั่ง และข้อความที่เข้ามาจะไม่ได้รับการประมวลผลและตอบกลับอีกต่อไป\n'
        'หากมีข้อสงสัยเกี่ยวกับข้อมูลที่ถูกจัดเก็บหรือเหตุผลในการยุติการให้บริการ '
        f'ท่านสามารถส่งคำร้องอย่างเป็นทางการไปยังผู้ดูแลโครงการได้ที่: {os.getenv("LINK_TO_ADMIN")}'
    ),
    # Swedish
    'sv': (
        '<b>Meddelande om nedläggning av tjänsten</b>\n\n'
        'Härmed meddelas att drift och teknisk support för denna programvara (bot) '
        'har upphört helt och permanent.\n'
        'Beslutet att ta systemet ur drift har fattats på grund av bristande efterfrågan '
        'på dess funktionalitet och avsaknad av motivering för fortsatt resursallokering '
        'för dess administration.\n'
        'Med omedelbar verkan har alla automatiserade processer stoppats, databaser arkiverats eller raderats '
        'och serverkapacitet omfördelats. '
        'Inkommande förfrågningar, kommandon och meddelanden behandlas inte längre och kommer inte att besvaras.\n'
        'För frågor gällande arkiverade data eller anledningen till tjänstens upphörande, '
        f'kan ni skicka en formell förfrågan till projektadministratören: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Bengali
    'bn': (
        '<b>পরিষেবা সমাপ্তির বিজ্ঞপ্তি</b>\n\n'
        'এতদ্বারা জানানো যাচ্ছে যে এই সফ্টওয়্যারটির (বট) পরিচালনা এবং প্রযুক্তিগত সহায়তা '
        'সম্পূর্ণরূপে এবং স্থায়ীভাবে বন্ধ করা হয়েছে।\n'
        'এর কার্যকারিতার প্রকৃত চাহিদার অভাব এবং এর প্রশাসনের জন্য সম্পদ বরাদ্দ চালিয়ে যাওয়ার '
        'যৌক্তিকতার অভাবে সিস্টেমটি বন্ধ করার সিদ্ধান্ত নেওয়া হয়েছে।\n'
        'তাৎক্ষণিকভাবে, সমস্ত স্বয়ংক্রিয় প্রক্রিয়া বন্ধ করা হয়েছে, ডেটাবেসগুলি আর্কাইভ বা মুছে ফেলা হয়েছে, '
        'এবং সার্ভারের ক্ষমতা পুনর্বন্টন করা হয়েছে। '
        'আগত অনুরোধ, কমান্ড এবং বার্তাগুলি আর প্রক্রিয়া করা হচ্ছে না এবং এর উত্তর দেওয়া হবে না।\n'
        'আর্কাইভ করা ডেটা বা পরিষেবা বন্ধের কারণ সম্পর্কিত যেকোনো অনুসন্ধানের জন্য, '
        f'আপনি প্রকল্প প্রশাসকের কাছে একটি আনুষ্ঠানিক অনুরোধ পাঠাতে পারেন: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Persian (Farsi)
    'fa': (
        '<b>اطलाعیه خاتمه خدمات</b>\n\n'
        'بدینوسیله به اطلاع می‌رساند که عملیات و پشتیبانی فنی این نرم‌افزار (ربات) '
        'به طور کامل و دائم متوقف شده است.\n'
        'تصمیم برای از رده خارج کردن سیستم به دلیل فقدان تقاضای واقعی برای عملکرد آن '
        'و نبود توجیه برای تخصیص منابع بیشتر جهت مدیریت آن اتخاذ گردیده است.\n'
        'از این لحظه، تمامی فرآیندهای خودکار متوقف شده، پایگاه‌های داده آرشیو یا حذف گردیده '
        'و ظرفیت سرور مجدداً تخصیص یافته است. '
        'درخواست‌ها، دستورات و پیام‌های ورودی دیگر پردازش نخواهند شد و پاسخی داده نمی‌شود.\n'
        'برای هرگونه سوال در مورد داده‌های آرشیو شده یا دلایل خاتمه خدمات، '
        f'می‌توانید یک درخواست رسمی به مدیر پروژه ارسال نمایید: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Urdu
    'ur': (
        '<b>سروس کے خاتمے کا نوٹس</b>\n\n'
        'آپ کو مطلع کیا جاتا ہے کہ اس سافٹ ویئر (بوٹ) کا آپریشن اور تکنیکی معاونت '
        'مکمل اور مستقل طور پر بند کر دی گئی ہے۔\n'
        'سسٹم کو غیر فعال کرنے کا فیصلہ اس کی فعالیت کی اصل طلب میں کمی '
        'اور اس کے انتظام کے لیے مزید وسائل مختص کرنے کے جواز نہ ہونے کی وجہ سے کیا گیا ہے۔\n'
        'فوری طور پر تمام خودکار عمل روک دیے گئے ہیں، ڈیٹا بیس کو آرکائیو یا حذف کر دیا گیا ہے، '
        'اور سرور کی گنجائش کو دوبارہ تقسیم کر دیا گیا ہے۔ '
        'اب آنے والی درخواستوں، کمانڈز اور پیغامات پر کارروائی نہیں کی جا رہی اور نہ ہی ان کا جواب دیا جائے گا۔\n'
        'آرکائیو شدہ ڈیٹا یا سروس کے خاتمے کی وجوہات سے متعلق کسی بھی سوال کے لیے، '
        f'آپ پروجیکٹ ایڈمنسٹریٹر کو باضابطہ درخواست بھیج سکتے ہیں: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Malay
    'ms': (
        '<b>Notis Penamatan Perkhidmatan</b>\n\n'
        'Harap maklum bahawa operasi dan sokongan teknikal untuk perisian (bot) ini '
        'telah dihentikan sepenuhnya dan secara kekal.\n'
        'Keputusan untuk menamatkan sistem ini dibuat kerana kurangnya permintaan sebenar '
        'terhadap fungsinya dan ketiadaan justifikasi untuk terus memperuntukkan sumber '
        'bagi pentadbirannya.\n'
        'Berkuat kuasa serta-merta, semua proses automatik telah dihentikan, pangkalan data telah diarkibkan atau dipadamkan, '
        'dan kapasiti pelayan telah diagihkan semula. '
        'Permintaan, arahan, dan mesej yang masuk tidak lagi diproses dan tidak akan dilayan.\n'
        'Untuk sebarang pertanyaan mengenai data yang diarkibkan atau rasional di sebalik penamatan perkhidmatan, '
        f'anda boleh mengemukakan permohonan rasmi kepada pentadbir projek: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Filipino (Tagalog)
    'tl': (
        '<b>Pabatid sa Pagwawakas ng Serbisyo</b>\n\n'
        'Ipinababatid sa inyo na ang operasyon at teknikal na suporta para sa software (bot) na ito '
        'ay ganap at permanenteng itinigil.\n'
        'Ang desisyon na alisin ang sistema ay bunga ng kakulangan ng aktwal na pangangailangan '
        'para sa gamit nito at kawalan ng katwiran para sa patuloy na paglalaan ng mga mapagkukunan '
        'sa pangangasiwa nito.\n'
        'Simula ngayon, ang lahat ng awtomatikong proseso ay itinigil na, ang mga database ay na-archive o binura, '
        'at ang kapasidad ng server ay inilipat na sa iba. '
        'Ang mga papasok na kahilingan, utos, at mensahe ay hindi na pinoproseso at hindi na tutugunan.\n'
        'Para sa anumang katanungan tungkol sa naka-archive na data o sa mga dahilan ng pagwawakas ng serbisyo, '
        f'maaari kayong magpadala ng pormal na kahilingan sa administrator ng proyekto: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Swahili
    'sw': (
        '<b>Ilani ya Kusitishwa kwa Huduma</b>\n\n'
        'Tunapenda kuwataarifu kuwa uendeshaji na msaada wa kiufundi kwa programu hii (roboti) '
        'umesitishwa kabisa na kwa kudumu.\n'
        'Uamuzi wa kuondoa mfumo huu umefikiwa kutokana na ukosefu wa mahitaji halisi '
        'ya utendaji wake na kutokuwepo kwa uhalali wa kuendelea kutenga rasilimali '
        'kwa ajili ya usimamizi wake.\n'
        'Kuanzia sasa, michakato yote ya kiotomatiki imesimamishwa, hifadhidata imehifadhiwa au kufutwa, '
        'na uwezo wa seva umepangiwa matumizi mengine. '
        'Maombi, amri, na ujumbe unaoingia haushughulikiwi tena na hautajibiwa.\n'
        'Kwa maswali yoyote kuhusu data iliyohifadhiwa au sababu za kusitishwa kwa huduma, '
        f'unaweza kuwasilisha ombi rasmi kwa msimamizi wa mradi: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Romanian
    'ro': (
        '<b>Notificare privind încetarea serviciului</b>\n\n'
        'Prin prezenta vă informăm că operarea și asistența tehnică pentru acest software (bot) '
        'au fost întrerupte complet și definitiv.\n'
        'Decizia de a scoate sistemul din uz a fost luată din cauza lipsei de cerere reală '
        'pentru funcționalitățile sale și a lipsei de justificare pentru alocarea continuă de resurse '
        'pentru administrarea acestuia.\n'
        'Începând cu acest moment, toate procesele automate au fost oprite, bazele de date arhivate sau șterse, '
        'iar capacitatea serverului a fost redistribuită. '
        'Solicitările, comenzile și mesajele primite nu mai sunt procesate și nu vor primi răspuns.\n'
        'Pentru orice întrebări referitoare la datele arhivate sau motivele încetării serviciului, '
        f'puteți trimite o solicitare oficială administratorului de proiect: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Greek
    'el': (
        '<b>Ειδοποίηση Τερματισμού Υπηρεσίας</b>\n\n'
        'Σας ενημερώνουμε ότι η λειτουργία και η τεχνική υποστήριξη για αυτό το λογισμικό (bot) '
        'έχουν διακοπεί πλήρως και οριστικά.\n'
        'Η απόφαση για τον παροπλισμό του συστήματος ελήφθη λόγω της έλλειψης πραγματικής ζήτησης '
        'για τις λειτουργίες του και της απουσίας δικαιολογίας για την περαιτέρω διάθεση πόρων '
        'για τη διαχείρισή του.\n'
        'Με άμεση ισχύ, όλες οι αυτοματοποιημένες διαδικασίες έχουν σταματήσει, οι βάσεις δεδομένων έχουν αρχειοθετηθεί ή διαγραφεί '
        'και η χωρητικότητα του διακομιστή έχει ανακατανεμηθεί. '
        'Τα εισερχόμενα αιτήματα, εντολές και μηνύματα δεν επεξεργάζονται πλέον και δεν θα απαντηθούν.\n'
        'Για τυχόν ερωτήσεις σχετικά με αρχειοθετημένα δεδομένα ή τους λόγους τερματισμού της υπηρεσίας, '
        f'μπορείτε να υποβάλετε επίσημο αίτημα στον διαχειριστή του έργου: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Hebrew
    'he': (
        '<b>הודעה על הפסקת שירות</b>\n\n'
        'לידיעתכם, הפעילות והתמיכה הטכנית עבור תוכנה זו (בוט) '
        'הופסקו באופן מלא ולצמיתות.\n'
        'ההחלטה להשבית את המערכת התקבלה עקב היעדר ביקוש ממשי '
        'לפונקציונליות שלה והיעדר הצדקה להמשך הקצאת משאבים '
        'לניהולה.\n'
        'החל מרגע זה, כל התהליכים האוטומטיים נעצרו, מסדי הנתונים הועברו לארכיון או נמחקו, '
        'וקיבולת השרת הוקצתה מחדש. '
        'בקשות, פקודות והודעות נכנסות אינן מעובדות עוד ולא ייענו.\n'
        'לכל שאלה בנוגע לנתונים בארכיון או לסיבות להפסקת השירות, '
        f'ניתן להגיש בקשה רשמית למנהל הפרויקט: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Czech
    'cs': (
        '<b>Oznámení o ukončení poskytování služeb</b>\n\n'
        'Tímto vás informujeme, že provoz a technická podpora tohoto softwaru (bota) '
        'byly zcela a trvale ukončeny.\n'
        'Rozhodnutí o vyřazení systému z provozu bylo přijato z důvodu nedostatečné skutečné poptávky '
        'po jeho funkcích a neexistence odůvodnění pro další přidělování zdrojů '
        'na jeho správu.\n'
        'S okamžitou platností byly všechny automatizované procesy zastaveny, databáze archivovány nebo odstraněny '
        'a kapacita serveru byla přerozdělena. '
        'Příchozí požadavky, příkazy a zprávy již nejsou zpracovávány a nebude na ně odpovídáno.\n'
        'V případě jakýchkoli dotazů týkajících se archivovaných dat nebo důvodů ukončení služby '
        f'můžete zaslat oficiální žádost správci projektu: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Hungarian
    'hu': (
        '<b>Értesítés a szolgáltatás megszüntetéséről</b>\n\n'
        'Ezúton tájékoztatjuk, hogy a jelen szoftver (bot) működtetése és műszaki támogatása '
        'teljes mértékben és véglegesen megszűnt.\n'
        'A rendszer leállítására vonatkozó döntés a funkciói iránti tényleges kereslet hiánya, '
        'valamint az adminisztrációra fordított erőforrások további fenntartásának indokolatlansága miatt született.\n'
        'A mai nappal minden automatizált folyamat leállt, az adatbázisok archiválásra vagy törlésre kerültek, '
        'a szerverkapacitás pedig átcsoportosításra került. '
        'A beérkező kérések, parancsok és üzenetek feldolgozása megszűnt, azokra válaszolni nem áll módunkban.\n'
        'Az archivált adatokkal vagy a szolgáltatás megszüntetésének okaival kapcsolatos kérdéseivel '
        f'hivatalos kérelemmel fordulhat a projekt adminisztrátorához: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Finnish
    'fi': (
        '<b>Ilmoitus palvelun päättymisestä</b>\n\n'
        'Ilmoitamme täten, että tämän ohjelmiston (botin) toiminta ja tekninen tuki '
        'on lopetettu kokonaan ja pysyvästi.\n'
        'Päätös järjestelmän käytöstä poistamisesta tehtiin, koska sen toiminnoille ei ollut todellista kysyntää '
        'eikä resurssien kohdentaminen sen ylläpitoon ollut enää perusteltua.\n'
        'Kaikki automaattiset prosessit on pysäytetty välittömästi, tietokannat on arkistoitu tai poistettu '
        'ja palvelinkapasiteetti on jaettu uudelleen. '
        'Saapuvia pyyntöjä, komentoja ja viestejä ei enää käsitellä, eikä niihin vastata.\n'
        'Jos teillä on kysyttävää arkistoiduista tiedoista tai palvelun lopettamisen syistä, '
        f'voitte lähettää virallisen pyynnön projektin ylläpitäjälle: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Danish
    'da': (
        '<b>Meddelelse om ophør af service</b>\n\n'
        'Vi informerer hermed om, at driften og den tekniske support for denne software (bot) '
        'er blevet fuldstændigt og permanent indstillet.\n'
        'Beslutningen om at tage systemet ud af drift er truffet på baggrund af manglende faktisk efterspørgsel '
        'efter dets funktionalitet og manglende berettigelse til fortsat ressourceallokering '
        'til administrationen heraf.\n'
        'Med øjeblikkelig virkning er alle automatiserede processer stoppet, databaser er arkiveret eller slettet, '
        'og serverkapacitet er omfordelt. '
        'Indgående anmodninger, kommandoer og beskeder behandles ikke længere og vil ikke blive besvaret.\n'
        'For spørgsmål vedrørende arkiverede data eller årsagerne til tjenestens ophør, '
        f'kan du sende en formel anmodning til projektadministratoren: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Norwegian
    'no': (
        '<b>Varsel om avvikling av tjenesten</b>\n\n'
        'Vi informerer herved om at drift og teknisk støtte for denne programvaren (boten) '
        'er fullstendig og permanent avsluttet.\n'
        'Beslutningen om å ta systemet ut av drift ble tatt på grunn av manglende faktisk etterspørsel '
        'etter funksjonaliteten, samt manglende grunnlag for videre tildeling av ressurser '
        'til administrasjon.\n'
        'Alle automatiserte prosesser er nå stoppet, databaser er arkivert eller slettet, '
        'og serverkapacitet er omdisponert. '
        'Innkommende forespørsler, kommandoer og meldinger behandles ikke lenger og vil ikke bli besvart.\n'
        'For spørsmål vedrørende arkiverte data eller årsaken til at tjenesten opphører, '
        f'kan du sende en formell henvendelse til prosjektadministratoren: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Slovak
    'sk': (
        '<b>Oznámenie o ukončení poskytovania služieb</b>\n\n'
        'Týmto vás informujeme, že prevádzka a technická podpora tohto softvéru (bota) '
        'boli úplne a natrvalo ukončené.\n'
        'Rozhodnutie o vyradení systému z prevádzky bolo prijaté z dôvodu nedostatočného skutočného dopytu '
        'po jeho funkciách a neexistencie opodstatnenia pre ďalšie vyčleňovanie zdrojov '
        'na jeho správu.\n'
        'S okamžitou platnosťou boli všetky automatizované procesy zastavené, databázy archivované alebo vymazané '
        'a kapacita servera bola prerozdelená. '
        'Prichádzajúce žiadosti, príkazy a správy sa už nespracúvajú a nebude sa na ne odpovedať.\n'
        'V prípade akýchkoľvek otázok týkajúcich sa archivovaných údajov alebo dôvodov ukončenia služby '
        f'môžete zaslať oficiálnu žiadosť správcovi projektu: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Bulgarian
    'bg': (
        '<b>Уведомление за прекратяване на услугата</b>\n\n'
        'С настоящото ви уведомяваме, че експлоатацията и техническата поддръжка на този софтуер (бот) '
        'са напълно и окончателно преустановени.\n'
        'Решението за извеждане на системата от експлоатация е взето поради липса на реално търсене '
        'на функционалността ѝ и липса на обосновка за по-нататъшно разходване на ресурси '
        'за нейното администриране.\n'
        'Към момента всички автоматизирани процеси са спрени, базите данни са архивирани или изтрити, '
        'а сървърните мощности са преразпределени. '
        'Входящите заявки, команди и съобщения вече не се обработват и на тях няма да бъде отговаряно.\n'
        'За всякакви въпроси, касаещи архивирани данни или причините за прекратяване на дейността, '
        f'можете да изпратите официално запитване до администратора на проекта: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Serbian (Cyrillic)
    'sr': (
        '<b>Обавештење о престанку пружања услуге</b>\n\n'
        'Овим вас обавештавамо да су рад и техничка подршка за овај софтвер (бот) '
        'потпуно и трајно обустављени.\n'
        'Одлука о стављању система ван погона донета је услед недостатка стварне потражње '
        'за његовим функцијама и одсуства оправдања за даље додељивање ресурса '
        'за његову администрацију.\n'
        'Са тренутним дејством, сви аутоматизовани процеси су заустављени, базе података су архивиране или обрисане, '
        'а капацитети сервера су прерасподељени. '
        'Долазни захтеви, команде и поруке се више не обрађују и на њих неће бити одговорено.\n'
        'За сва питања у вези са архивираним подацима или разлозима за прекид рада, '
        f'можете послати званичан захтев администратору пројекта: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Croatian
    'hr': (
        '<b>Obavijest o prestanku pružanja usluge</b>\n\n'
        'Ovim vas obavještavamo da su rad i tehnička podrška za ovaj softver (bot) '
        'potpuno i trajno obustavljeni.\n'
        'Odluka o povlačenju sustava iz upotrebe donesena je zbog nedostatka stvarne potražnje '
        'za njegovim funkcionalnostima i nepostojanja opravdanja za daljnju alokaciju resursa '
        'za njegovu administraciju.\n'
        'S trenutnim učinkom, svi automatizirani procesi su zaustavljeni, baze podataka arhivirane ili izbrisane, '
        'a kapaciteti poslužitelja preraspodijeljeni. '
        'Dolazni zahtjevi, naredbe i poruke više se ne obrađuju i na njih se neće odgovarati.\n'
        'Za sva pitanja vezana uz arhivirane podatke ili razloge prestanka rada, '
        f'možete poslati službeni zahtjev administratoru projekta: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Uzbek
    'uz': (
        '<b>Xizmat ko‘rsatish to‘xtatilganligi haqida bildirishnoma</b>\n\n'
        'Ushbu bilan shuni ma’lum qilamizki, mazkur dasturiy ta’minot (bot) faoliyati va texnik qo‘llab-quvvatlanishi '
        'to‘liq va butunlay to‘xtatildi.\n'
        'Tizimni foydalanishdan chiqarish to‘g‘risidagi qaror uning funksionalligiga bo‘lgan haqiqiy talabning yo‘qligi '
        'va uni boshqarish uchun resurslarni sarflashni davom ettirish maqsadga muvofiq emasligi sababli qabul qilindi.\n'
        'Hozirgi vaqtda barcha avtomatlashtirilgan jarayonlar to‘xtatildi, ma’lumotlar bazalari arxivlandi yoki o‘chirib tashlandi, '
        'server quvvatlari esa qayta taqsimlandi. '
        'Kiruvchi so‘rovlar, buyruqlar va xabarlar endi qayta ishlanmaydi va ularga javob berilmaydi.\n'
        'Arxivlangan ma’lumotlar yoki faoliyat to‘xtatilishining sabablari bo‘yicha har qanday savollar bilan '
        f'loyiha administratoriga rasmiy so‘rov yuborishingiz mumkin: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Kazakh
    'kk': (
        '<b>Қызмет көрсетудің тоқтатылуы туралы хабарлама</b>\n\n'
        'Осы арқылы бұл бағдарламалық жасақтаманы (ботты) пайдалану және оған техникалық қолдау көрсету '
        'толығымен және түпкілікті тоқтатылғанын хабарлаймыз.\n'
        'Жүйені пайдаланудан шығару туралы шешім оның функционалдығына нақты сұраныстың болмауына '
        'жана оны әкімшілендіруге ресурстарды одан әрі бөлудің орынсыздығына байланысты қабылданды.\n'
        'Қазіргі уақытта барлық автоматтандырылған процестер тоқтатылды, дерекқорлар мұрағатталды немесе жойылды, '
        'ал сервер қуаттары қайта бөлінді. '
        'Келип түскен сұраулар, пәрмендер мен хабарламалар бұдан былай өңделмейді және жауапсыз қалады.\n'
        'Мұрағатталған деректерге немесе жұмысты тоқтату себептеріне қатысты кез келген сұрақтар бойынша '
        f'жоба әкімшісіне ресми сұрау жібере аласыз: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Lithuanian
    'lt': (
        '<b>Pranešimas apie paslaugos teikimo nutraukimą</b>\n\n'
        'Šiuo pranešame, kad šios programinės įrangos (boto) veikimas ir techninis palaikymas '
        'buvo visiškai ir visam laikui nutraukti.\n'
        'Sprendimas nutraukti sistemos eksploatavimą buvo priimtas dėl nepakankamos faktinės paklausos '
        'jos funkcijoms ir tolesnio išteklių skyrimo administravimui nepagrįstumo.\n'
        'Nuo šio momento visi automatizuoti procesai sustabdyti, duomenų bazės archyvuotos arba ištrintos, '
        'o serverio pajėgumai perskirstyti. '
        'Gaunamos užklausos, komandos ir pranešimai nebėra apdorojami ir į juos nebus atsakoma.\n'
        'Kilus klausimams dėl archyvuotų duomenų ar veiklos nutraukimo priežasčių, '
        f'galite pateikti oficialų prašymą projekto administratoriui: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Slovenian
    'sl': (
        '<b>Obvestilo o prenehanju delovanja storitve</b>\n\n'
        'Obveščamo vas, da sta delovanje in tehnična podpora za to programsko opremo (bota) '
        'popolnoma in trajno ukinjena.\n'
        'Odločitev za ukinitev sistema je bila sprejeta zaradi pomanjkanja dejanskega povpraševanja '
        'po njegovi funkcionalnosti in odsotnosti upravičenosti za nadaljnje dodeljevanje sredstev '
        'za njegovo upravljanje.\n'
        'S takojšnjim učinkom so vsi avtomatizirani procesi ustavljeni, podatkovne baze arhivirane ali izbrisane, '
        'zmogljivosti strežnika pa prerazporejene. '
        'Dohodne zahteve, ukazi in sporočila se ne obdelujejo več in nanje ne bomo odgovarjali.\n'
        'Za vsa vprašanja glede arhiviranih podatkov ali razlogov za prenehanje delovanja '
        f'lahko pošljete uradno zahtevo administratorju projekta: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Azerbaijani (Azerbaijan)
    'az': (
        '<b>Xidmətin dayandırılması haqqında bildiriş</b>\n\n'
        'Nəzərinizə çatdırırıq ki, bu proqram təminatının (botun) istismarı və texniki dəstəyi '
        'tam və birdəfəlik dayandırılmışdır.\n'
        'Sistemin istismardan çıxarılması barədə qərar, onun funksionallığına faktiki tələbatın olmaması '
        'və idarəetmə üçün resursların ayrılmasının davam etdirilməsinin məqsədəuyğunsuzluğu səbəbindən qəbul edilmişdir.\n'
        'Hazırda bütün avtomatlaşdırılmış proseslər dayandırılıb, verilənlər bazaları arxivləşdirilib və ya silinib, '
        'server gücləri isə yenidən paylanıb. '
        'Daxil olan sorğular, əmrlər və mesajlar artıq emal olunmur və cavablandırılmayacaq.\n'
        'Arxivlənmiş məlumatlar və ya fəaliyyətin dayandırılması səbəbləri ilə bağlı hər hansı sualınız olarsa, '
        f'layihə inzibatçısına rəsmi sorğu göndərə bilərsiniz: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Kyrgyz (Kyrgyzstan)
    'ky': (
        '<b>Кызмат көрсөтүүнү токтотуу жөнүндө билдирүү</b>\n\n'
        'Ушуну менен сизге бул программалык камсыздоону (ботту) иштетүү жана техникалык колдоо '
        'толугу менен жана биротоло токтотулгандыгын маалымдайбыз.\n'
        'Тутумду колдонуудан чыгаруу чечими анын функцияларына болгон реалдуу суроо-талаптын жоктугуна '
        'жана аны башкарууга ресурстарды бөлүштүрүүнү улантуунун максатка ылайыксыздыгына байланыштуу кабыл алынды.\n'
        'Учурда бардык автоматташтырылган процесстер токтотулуп, маалымат базалары архивделди же өчүрүлдү, '
        'ал эми сервердик кубаттуулуктар кайра бөлүштүрүлдү. '
        'Келип түшкөн суроо-талаптар, буйруктар жана билдирүүлөр мындан ары иштелип чыкпайт жана жооп берилбейт.\n'
        'Архивделген маалыматтар же кызматты токтотуу себептери боюнча суроолоруңуз болсо, '
        f'долбоордун администраторуна расмий суроо-талап жөнөтсөңүз болот: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Tajik (Tajikistan)
    'tg': (
        '<b>Огоҳинома дар бораи қатъи хидматрасонӣ</b>\n\n'
        'Ба маълумоти шумо мерасонем, ки истифода ва дастгирии техникии ин нармафзор (бот) '
        'пурра ва ниҳоят қатъ карда шудааст.\n'
        'Қарор дар бораи қатъи фаъолияти система бинобар набудани талаботи воқеӣ ба вазифаҳои он '
        'ва ғайримақсаднок будани сарфи минбаъдаи захираҳо барои идоракунии он қабул шудааст.\n'
        'Дар ҳоли ҳозир тамоми равандҳои автоматӣ боздошта шудаанд, пойгоҳҳои маълумот бойгонӣ ё нест карда шудаанд '
        'ва иқтидори серверҳо аз нав тақсим карда шудаанд. '
        'Дархостҳо, фармонҳо ва паёмҳои воридотӣ дигар коркард намешаванд ва ба онҳо ҷавоб дода намешавад.\n'
        'Барои ҳама гуна саволҳо оид ба маълумоти бойгонӣ ё сабабҳои қатъи кор, '
        f'шумо метавонед ба маъмури лоиҳа дархости расмӣ фиристед: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Belarusian (Belarus)
    'be': (
        '<b>Паведамленне аб спыненні абслугоўвання</b>\n\n'
        'Даводзім да вашага ведама, што эксплуатацыя і тэхнічная падтрымка гэтага праграмнага забеспячэння (бота) '
        'былі цалкам і канчаткова спыненыя.\n'
        'Рашэнне аб вывадзе сістэмы з эксплуатацыі прынята ў сувязі з адсутнасцю фактычнай запатрабаванасці функцыяналу '
        'і мэтазгоднасці далейшага расходавання рэсурсаў на адміністраванне.\n'
        'На дадзены момант усе аўтаматызаваныя працэсы спынены, базы дадзеных заархіваваны або выдалены, '
        'а серверныя магутнасці пераразмеркаваны. '
        'Уваходныя запыты, каманды і паведамленні больш не апрацоўваюцца, адказы на іх давацца не будуць.\n'
        'Па ўсіх пытаннях, якія тычацца архіўных дадзеных або прычын спынення працы, '
        f'вы можаце накіраваць афіцыйны запыт адміністратару праекта: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Georgian (Georgia)
    'ka': (
        '<b>შეტყობინება მომსახურების შეწყვეტის შესახებ</b>\n\n'
        'გაცნობებთ, რომ ამ პროგრამული უზრუნველყოფის (ბოტის) მუშაობა და ტექნიკური მხარდაჭერა '
        'სრულად და საბოლოოდ შეწყვეტილია.\n'
        'სისტემის ექსპლუატაციიდან ამოღების გადაწყვეტილება მიღებულ იქნა მისი ფუნქციონალის მიმართ რეალური მოთხოვნის არარსებობისა '
        'და ადმინისტრირებისთვის რესურსების შემდგომი გამოყოფის მიზანშეწონილობის ნაკლებობის გამო.\n'
        'ამ დროისთვის ყველა ავტომატიზებული პროცესი გაჩერებულია, მონაცემთა ბაზები დაარქივებული ან წაშლილია, '
        'ხოლო სერვერის სიმძლავრეები გადანაწილებულია. '
        'შემოსული მოთხოვნები, ბრძანებები და შეტყობინებები აღარ მუშავდება და მათზე პასუხი არ გაიცემა.\n'
        'დაარქივებულ მონაცემებთან ან სერვისის შეწყვეტის მიზეზებთან დაკავშირებული ნებისმიერი კითხვის შემთხვევაში, '
        f'შეგიძლიათ გაუგზავნოთ ოფიციალური მოთხოვნა პროექტის ადმინისტრატორს: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Armenian (Armenia)
    'hy': (
        '<b>Ծանուցում ծառայության դադարեցման մասին</b>\n\n'
        'Սույնով տեղեկացնում ենք, որ այս ծրագրային ապահովման (բոտի) շահագործումը և տեխնիկական աջակցությունը '
        'ամբողջությամբ և վերջնականապես դադարեցվել են:\n'
        'Համակարգը շահագործումից հանելու որոշումը կայացվել է դրա ֆունկցիոնալության նկատմամբ փաստացի պահանջարկի բացակայության '
        'և կառավարման համար ռեսուրսների հետագա հատկացման աննպատակահարմարության պատճառով:\n'
        'Այս պահին բոլոր ավտոմատացված գործընթացները կասեցված են, տվյալների բազաները արխիվացված կամ ջնջված են, '
        'իսկ սերվերային հզորությունները վերաբաշխված են: '
        'Մուտքային հարցումները, հրամանները և հաղորդագրությունները այլևս չեն մշակվում և չեն պատասխանվի:\n'
        'Արխիվացված տվյալների կամ ծառայության դադարեցման պատճառների վերաբերյալ ցանկացած հարցով '
        f'կարող եք պաշտոնական հարցում ուղարկել նախագծի ադմինիստրատորին՝ {os.getenv("LINK_TO_ADMIN")}:'
    ),
    # Amharic (Ethiopia)
    'am': (
        '<b>የአገልግሎት ማቋረጥ ማስታወቂያ</b>\n\n'
        'የዚህ ሶፍትዌር (ቦት) ኦፕሬሽን እና ቴክኒካዊ ድጋፍ ሙሉ በሙሉ እና በቋሚነት መቋረጡን እናሳውቃለን።\n'
        'ስርዓቱን ከአገልግሎት ውጪ ለማድረግ የተወሰነው ለአገልግሎቱ ትክክለኛ ፍላጎት ባለመኖሩ '
        'እና ለርሱ አስተዳደር ተጨማሪ ሀብቶችን መመደብ አግባብነት ስለሌለው ነው።\n'
        'በአሁኑ ጊዜ ሁሉም ራስ-ሰር ሂደቶች ቆመዋል፣ የውሂብ ጎታዎች ተቀምጠዋል ወይም ተሰርዘዋል፣ '
        'እንዲሁም የሰርቨር አቅም ለሌላ አገልግሎት ተመድቧል። '
        'የሚገቡ ጥያቄዎች፣ ትዕዛዞች እና መልዕክቶች ከእንግዲህ አይስተናገዱም እንዲሁም ምላሽ አይሰጥባቸውም።\n'
        'ስለተቀመጡ መረጃዎች ወይም ስለ አገልግሎቱ መቋረጥ ምክንያቶች ማንኛውም ጥያቄ ካለዎት፣ '
        f'ለፕሮጀክቱ አስተዳዳሪ ኦፊሴላዊ ጥያቄ ማቅረብ ይችላሉ፡ {os.getenv("LINK_TO_ADMIN")}።'
    ),
    # Khmer (Cambodia)
    'km': (
        '<b>សេចក្តីជូនដំណឹងអំពីការបញ្ឈប់សេវាកម្ម</b>\n\n'
        'សូមជម្រាបជូនថា ប្រតិបត្តិការ និងការគាំទ្រផ្នែកបច្ចេកទេសសម្រាប់កម្មវិធី (bot) នេះត្រូវបានបញ្ឈប់ទាំងស្រុង និងជាអចិន្ត្រៃយ៍។\n'
        'ការសម្រេចចិត្តបិទប្រព័ន្ធនេះ ត្រូវបានធ្វើឡើងដោយសារតែខ្វះតម្រូវការជាក់ស្តែងសម្រាប់ការប្រើប្រាស់ '
        'និងកង្វះហេតុផលសមស្របសម្រាប់ការបន្តចំណាយធនធានលើការគ្រប់គ្រង។\n'
        'គិតត្រឹមពេលនេះ រាល់ដំណើរការស្វ័យប្រវត្តិទាំងអស់ត្រូវបានបញ្ឈប់ មូលដ្ឋានទិន្នន័យត្រូវបានរក្សាទុកក្នុងបណ្ណសារ ឬលុបចោល '
        'ហើយសមត្ថភាពម៉ាស៊ីនមេត្រូវបានបែងចែកឡើងវិញ។ '
        'សំណើ បញ្ជា និងសារដែលចូលមក នឹងលែងត្រូវបានដំណើរការ ហើយនឹងមិនត្រូវបានឆ្លើយតបឡើយ។\n'
        'សម្រាប់សំណួរណាមួយទាក់ទងនឹងទិន្នន័យដែលបានរក្សាទុក ឬមូលហេតុនៃការបញ្ឈប់សេវាកម្ម '
        f'អ្នកអាចផ្ញើសំណើជាផ្លូវការទៅកាន់អ្នកគ្រប់គ្រងគម្រោង៖ {os.getenv("LINK_TO_ADMIN")}។'
    ),
    # Latvian
    'lv': (
        '<b>Paziņojums par pakalpojuma pārtraukšanu</b>\n\n'
        'Ar šo informējam, ka šīs programmatūras (bota) darbība un tehniskais atbalsts '
        'ir pilnībā un neatgriezeniski pārtraukts.\n'
        'Lēmums par sistēmas ekspluatācijas pārtraukšanu tika pieņemts sakarā ar reāla pieprasījuma trūkumu '
        'pēc tās funkcionalitātes un pamatojuma neesamību turpmākai resursu piešķiršanai tās administrēšanai.\n'
        'Šobrīd visi automatizētie procesi ir apturēti, datu bāzes ir arhivētas vai dzēstas, '
        'un servera jaudas ir pārdalītas. '
        'Ienākošie pieprasījumi, komandas un ziņojumi vairs netiek apstrādāti un uz tiem netiks atbildēts.\n'
        'Jautājumu gadījumā par arhivētajiem datiem vai darbības pārtraukšanas iemesliem, '
        f'varat nosūtīt oficiālu pieprasījumu projekta administratoram: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Estonian
    'et': (
        '<b>Teade teenuse osutamise lõpetamisest</b>\n\n'
        'Käesolevaga teavitame teid, et selle tarkvara (boti) töö ja tehniline tugi '
        'on täielikult ja lõplikult lõpetatud.\n'
        'Otsus süsteemi kasutusest kõrvaldamiseks võeti vastu seoses tegeliku nõudluse puudumisega selle funktsionaalsuse järele '
        'ning ressursside edasise eraldamise põhjendamatusega selle haldamiseks.\n'
        'Hetkel on kõik automatiseeritud protsessid peatatud, andmebaasid arhiveeritud või kustutatud '
        'ning serveri ressursid ümber jaotatud. '
        'Sissetulevaid päringuid, käsklusi ja sõnumeid enam ei töödelda ning neile ei vastata.\n'
        'Kõigi arhiveeritud andmeid või tegevuse lõpetamise põhjuseid puudutavate küsimuste korral '
        f'võite saata ametliku päringu projekti administraatorile: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Burmese
    'my': (
        '<b>ဝန်ဆောင်မှုရပ်ဆိုင်းကြောင်း အသိပေးချက်</b>\n\n'
        'ဤဆော့ဖ်ဝဲ (bot) ၏ လုပ်ငန်းဆောင်ရွက်မှုနှင့် နည်းပညာပံ့ပိုးမှုများကို '
        'လုံးဝ (အပြီးအပိုင်) ရပ်ဆိုင်းလိုက်ပြီဖြစ်ကြောင်း အသိပေးအပ်ပါသည်။\n'
        'စနစ်ကို ရပ်ဆိုင်းရန် ဆုံးဖြတ်ချက်သည် ၎င်း၏လုပ်ဆောင်ချက်များအတွက် အမှန်တကယ် လိုအပ်ချက်မရှိတော့ခြင်းနှင့် '
        'စီမံခန့်ခွဲမှုအတွက် အရင်းအမြစ်များကို ဆက်လက်အသုံးပြုရန် အကြောင်းပြချက်ခိုင်လုံမှုမရှိခြင်းတို့ကြောင့် ဖြစ်ပါသည်။\n'
        'ယခုအချိန်တွင် အလိုအလျောက်လုပ်ဆောင်မှုများအားလုံးကို ရပ်တန့်ထားပြီး၊ ဒေတာဘေ့စ်များကို သိမ်းဆည်းထားခြင်း သို့မဟုတ် ဖျက်သိမ်းခြင်းများ ပြုလုပ်ထားပြီးဖြစ်ကာ '
        'ဆာဗာစွမ်းရည်များကို နေရာပြန်လည်ခွဲဝေထားပါသည်။ '
        'ဝင်ရောက်လာသော တောင်းဆိုမှုများ၊ ညွှန်ကြားချက်များနှင့် မက်ဆေ့ချ်များကို ဆက်လက်လုပ်ဆောင်တော့မည် မဟုတ်သလို ဖြေကြားပေးမည်လည်း မဟုတ်ပါ။\n'
        'သိမ်းဆည်းထားသော အချက်အလက်များ သို့မဟုတ် ဝန်ဆောင်မှုရပ်ဆိုင်းရသည့် အကြောင်းရင်းများနှင့် ပတ်သက်၍ မေးမြန်းလိုသည်များရှိပါက '
        f'ပရောဂျက် စီမံခန့်ခွဲသူထံသို့ တရားဝင် စာပို့မေးမြန်းနိုင်ပါသည်: {os.getenv("LINK_TO_ADMIN")}.'
    ),
    # Tamil
    'ta': (
        '<b>சேவை நிறுத்த அறிவிப்பு</b>\n\n'
        'இந்த மென்பொருளின் (bot) செயல்பாடு மற்றும் தொழில்நுட்ப ஆதரவு '
        'முழுமையாகவும் நிரந்தரமாகவும் நிறுத்தப்பட்டுள்ளது என்பதைத் தெரிவித்துக் கொள்கிறோம்.\n'
        'இதன் செயல்பாட்டிற்கான உண்மையான தேவை குறைந்துவிட்டதாலும், '
        'இதை நிர்வகிப்பதற்குத் தொடர்ந்து வளங்களை ஒதுக்குவதில் நியாயம் இல்லாததாலும் இந்த முடிவு எடுக்கப்பட்டுள்ளது.\n'
        'தற்போது, அனைத்து தானியங்கி செயல்முறைகளும் நிறுத்தப்பட்டுவிட்டன, தரவுத்தளங்கள் காப்பகப்படுத்தப்பட்டுள்ளன அல்லது அழிக்கப்பட்டுவிட்டன, '
        'மற்றும் சர்வர் வளங்கள் மறுஒதுக்கீடு செய்யப்பட்டுள்ளன. '
        'இனி வரும் கோரிக்கைகள், கட்டளைகள் மற்றும் செய்திகள் செயலாக்கப்படாது மற்றும் அவற்றுக்கு பதிலளிக்கப்படாது.\n'
        'காப்பகப்படுத்தப்பட்ட தரவு அல்லது சேவை நிறுத்தத்திற்கான காரணங்கள் தொடர்பான ஏதேனும் கேள்விகளுக்கு, '
        f'திட்ட நிர்வாகிக்கு நீங்கள் அதிகாரப்பூர்வ கோரிக்கையை அனுப்பலாம்: {os.getenv("LINK_TO_ADMIN")}.'
    ),
}
