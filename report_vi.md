# I. Strava

## 1. Giới thiệu

### a. Giới thiệu sản phẩm

Strava là một ứng dụng điện thoại và web dùng để theo dõi hoạt động thể chất. Người dùng bắt đầu ghi lại một buổi tập, và ứng dụng dùng GPS để ghi nhận quãng đường, thời gian, và tốc độ trong lúc họ đi bộ, chạy, hoặc đạp xe. Sau khi hoạt động kết thúc, Strava biến dữ liệu GPS thô thành các chỉ số thống kê (biểu đồ tốc độ, độ cao, kỷ lục cá nhân) và cho phép người dùng chia sẻ với bảng tin của bạn bè, gửi và nhận "kudos" (lời khen), hoặc tham gia câu lạc bộ và thử thách. Nói ngắn gọn, đây là một công cụ theo dõi GPS có thêm lớp mạng xã hội bên trên.

Báo cáo này dựa trên một phiên trải nghiệm thực tế lần đầu sử dụng ứng dụng, ở gói miễn phí trên iPhone: một lần đi bộ thật được ghi lại từ đầu đến cuối, cùng với việc khám phá các tab Maps (Bản đồ) và Groups (Nhóm) sau đó.

### b. Mục tiêu người dùng

Lý do chính khiến một người mở Strava rất đơn giản: **ghi lại một hoạt động và xem các con số cơ bản sau đó** — quãng đường, thời gian, tốc độ. Trải nghiệm trực tiếp trong dự án này xác nhận rõ điều này: giá trị cốt lõi của ứng dụng được cảm nhận đơn giản là "nhấn Start, Stop, Resume, Finish khi đi bộ." Mọi thứ khác — phân tích tốc độ chi tiết, khám phá lộ trình, câu lạc bộ, thử thách — chỉ được khám phá vì tò mò trong quá trình thử ứng dụng, không phải vì đó là nhu cầu ban đầu.

### c. Người dùng chính

Dữ liệu xu hướng của chính Strava cho thấy chạy bộ vẫn là môn thể thao được theo dõi nhiều nhất trên nền tảng, với đua xe đang tăng trưởng. Nhưng phần lớn người dùng không phải vận động viên thi đấu — Strava báo cáo rằng 93% người dùng nói động lực chính của họ là sức khỏe, không phải cạnh tranh. Vậy nên đối tượng chính gần với "những người muốn duy trì vận động và theo dõi tiến bộ của bản thân" hơn là "vận động viên đua nghiêm túc."

### d. Người dùng phụ

- Người đi bộ thông thường — đi bộ là hoạt động được ghi nhận nhiều thứ hai trên Strava, ngay sau chạy bộ. Người đi bộ trong phiên thử nghiệm của dự án này đại diện cho một phân khúc người dùng lớn, bình thường, chứ không phải trường hợp hiếm gặp.
- Người đạp xe, bơi lội, leo núi, và ba môn phối hợp (triathlete).
- Người dùng cạnh tranh, quan tâm đến bảng xếp hạng đoạn đường (segment) và dữ liệu tập luyện có cấu trúc.
- Người dùng thiên về mạng xã hội, tham gia câu lạc bộ và thử thách — nhóm này nghiêng về người dùng trẻ hơn (Gen Z).
- Người dùng đa môn thể thao: 54% người dùng theo dõi hơn một loại hoạt động, và 96% tham gia hơn một môn thể thao, nên việc chuyển đổi giữa các loại hoạt động là chuyện bình thường, không phải hiếm gặp.

### e. Yêu cầu về thiết bị và kiến thức

**Thiết bị**: điện thoại iOS hoặc Android, hoặc trang bảng điều khiển strava.com trên web. Phiên thử nghiệm cho báo cáo này dùng iPhone. Strava cũng hỗ trợ Wear OS, ghi hoạt động trên Apple Watch, và đồng bộ từ các thiết bị Garmin, Wahoo, Suunto, Polar, Fitbit, và Coros.

**Gói tài khoản**: Strava có gói Miễn phí (Free) và gói trả phí (Subscription). Gói Miễn phí — được dùng trong dự án này — bao gồm ghi lại hoạt động, tham gia cộng đồng, và các tính năng an toàn. Gói trả phí mở khóa lộ trình tùy chỉnh, bản đồ ngoại tuyến, lịch sử tập luyện đầy đủ, phân tích buổi tập chuyên sâu hơn, theo dõi mục tiêu, bảng xếp hạng đoạn đường, và điểm số thể lực. Người dùng miễn phí lần đầu gặp các lời mời nâng cấp khá thường xuyên: các biểu ngữ "Start a free trial" (Bắt đầu dùng thử miễn phí) hoặc "Subscribe" (Đăng ký) xuất hiện lặp lại ở tab Maps, màn hình Workout Analysis (Phân tích buổi tập), tab You/Progress (Bạn/Tiến độ), tab You/Workouts (Bạn/Buổi tập), và tab Groups trong phiên thử nghiệm.

**Kiến thức cần có trước**: không cần gì cho vòng lặp thao tác cốt lõi. Toàn bộ trình tự Start → Pause/Resume → Finish được hoàn thành ngay trong lần trải nghiệm đầu tiên, không hề do dự hay cần trợ giúp. Nhưng các màn hình phân tích phụ, bị khóa sau gói trả phí, thì không rõ ràng ngay từ lần nhìn đầu tiên.

---

## 2. Tình huống sử dụng 1: Ghi lại, Kết thúc, và Lưu một buổi Đi bộ ngoài trời

### a. Phân tích tình huống sử dụng 1

**Mục tiêu**: theo dõi quãng đường, thời gian, và tốc độ cho một buổi đi bộ theo thời gian thực, sau đó lưu lại thành một bản ghi lâu dài.
**Tác nhân kích hoạt**: mở tab Record và nhấn Start.
**Các bước quan sát được**:
1. Màn hình đang ghi hoạt động — bản đồ trực tiếp, số liệu trực tiếp (Time/Distance/Speed), nút Pause.
![In-progress recording screen](strava-images/IMG_0514.PNG)
*IMG_0514 — Màn hình đang ghi hoạt động: bản đồ trực tiếp với Time/Distance/Speed và một nút Pause.*
2. Nhấn Pause → Màn hình Dừng — hiển thị số liệu lớn (Distance, Avg Speed), nút Resume/Finish.
![Stopped screen](strava-images/IMG_0515.PNG)
*IMG_0515 — Màn hình Dừng: hiển thị số liệu lớn Distance/Avg Speed cùng nút Resume/Finish.*
3. Nhấn Finish → Save Activity, màn hình 1 (tiêu đề, mô tả, danh sách chọn loại hoạt động, xem trước bản đồ, thẻ tag).
![Save Activity screen 1](strava-images/IMG_0517.PNG)
*IMG_0517 — Save Activity màn hình 1: ô tiêu đề/mô tả, danh sách chọn loại Walk, xem trước bản đồ.*
4. Cuộn xuống Save Activity, màn hình 2 ("How did that feel?", ghi chú riêng tư, trang thiết bị, cài đặt Visibility, ô chọn Mute Activity, nút Save Activity).
![Save Activity screen 2](strava-images/IMG_0518.PNG)
*IMG_0518 — Save Activity màn hình 2: How did that feel, Visibility, Mute Activity, nút Save Activity.*
5. Nhấn Save Activity → hoạt ảnh chuyển cảnh "Nice work!".
![Nice work transition screen](strava-images/IMG_0519.PNG)
*IMG_0519 — Màn hình hoạt ảnh chuyển cảnh "Nice work!".*
6. → Cửa sổ bật lên thành tích hoạt động đầu tiên "Welcome to the team, Duy!" (View Activity / View in Trophy Case).
![First-activity achievement popup](strava-images/IMG_0520.PNG)
*IMG_0520 — Cửa sổ bật lên thành tích hoạt động đầu tiên "Welcome to the team, Duy!".*
7. → Bảng chia sẻ Share Activity tự động mở ra (thẻ bản đồ + số liệu, Share to Message/Strava Message/Strava Post/Copy Link/More).
![Share Activity sheet](strava-images/IMG_0522.PNG)
*IMG_0522 — Bảng Share Activity: thẻ bản đồ+số liệu với các lựa chọn Share to Message/Strava Post/Copy Link.*

Đó là **5 màn hình riêng biệt giữa lúc nhấn Finish và lúc đạt trạng thái ổn định cuối cùng** — không phải chỉ một lời xác nhận.

### b. Bối cảnh và cách người dùng tương tác với tình huống này qua giao diện

#### i. Bối cảnh 1

- **Ở đâu**: Ngoài trời, trên một con đường thật.
- **Khi nào**: Sáng sớm, khoảng 06:09–06:15.
- **Tình huống người dùng**: Đang đi bộ — đang di chuyển, không ngồi yên. Đây là hoạt động đầu tiên trên tài khoản này trên Strava, được xác nhận qua huy hiệu "Kudos on your first activity!" và cửa sổ bật lên "Welcome to the team, Duy!".
- **Cách tương tác**: Chạm một tay. Sự chú ý bị chia giữa việc quan sát đường phía trước và liếc xuống điện thoại để kiểm tra tốc độ và thời lượng.
- **Kết quả mong đợi**: Một bản ghi chính xác của buổi đi bộ (quãng đường, thời gian, lộ trình), được lưu lại để xem sau. Việc chia sẻ được kỳ vọng là tùy chọn, không phải tự động.

### c. Áp dụng nguyên lý HCI (Lợi ích & Hạn chế)

#### i. Khả năng con người

- **Lợi ích — thị giác trung tâm (foveal vision)**: Trong lúc di chuyển, chỉ có thể tranh thủ liếc nhanh xuống điện thoại rồi nhìn lại đường ngay. Màn hình đang ghi và màn hình Dừng đặt Time/Distance/Speed thành các con số lớn, tương phản cao, ở giữa màn hình — đúng vị trí mà cái liếc mắt đó rơi vào. Điều này hiệu quả vì mắt chỉ nhìn rõ chi tiết ở một vùng trung tâm nhỏ (fovea, hay hố mắt), nên một con số cần nằm đúng điểm trung tâm đó để được đọc chỉ trong một lần nhìn.
- **Hạn chế — phản hồi chỉ qua thị giác trong lúc đi bộ**: Việc xác nhận Pause/Resume/Finish chỉ dựa vào kênh thị giác — một nút đổi màu hoặc đổi nhãn. Phản hồi của con người có thể truyền qua thị giác, thính giác, hoặc xúc giác (rung), còn mắt thì đã bận quan sát đường đi rồi. Một tín hiệu chỉ qua thị giác buộc phải nhìn thêm một lần đúng vào lúc thiết kế lẽ ra nên giảm thiểu việc phải di chuyển mắt.

#### ii. Mô hình tư duy của người dùng

- **Lợi ích — khớp với một hành động ngoài đời thật**: Start → Pause/Resume → Finish ánh xạ trực tiếp vào "đi bộ, rồi dừng lại." Mô hình tư duy (mental model) là bức tranh mà một người dựng lên trong đầu về cách một thứ gì đó vận hành, dựa trên kinh nghiệm trước đó — ở đây không cần xây dựng mô hình mới nào cả. Điều này khớp với cảm nhận trực tiếp về giá trị cốt lõi của ứng dụng: đơn giản là "nhấn Start, Stop, Resume, Finish."
- **Hạn chế — Finish không có nghĩa là xong**: Kỳ vọng tự nhiên đối với Finish là "xong rồi — chuyển thẳng đến trang hoạt động." Nhưng thay vào đó, hệ thống chèn thêm bốn màn hình nữa (biểu mẫu Save, hoạt ảnh "Nice work!", cửa sổ bật lên thành tích, và bảng Share) trước khi đạt trạng thái ổn định. Đây là một điểm lệch rõ rệt so với kỳ vọng ban đầu: ngay sau khi nhấn Finish trên một buổi đi bộ, giao diện lại chuyển sang một màn hình chia sẻ hoạt động, tạo cảm giác bất ngờ vào đúng lúc lẽ ra đã cảm thấy hoàn tất. Điều này vi phạm Quy tắc vàng số 4 của Shneiderman, "thiết kế các hộp thoại để tạo cảm giác khép lại" (design dialogs to yield closure) — một luồng thao tác nên tạo cảm giác đã đến một điểm kết thúc rõ ràng, chứ không kéo thêm các bước ngay đúng lúc lẽ ra đã xong.

#### iii. Ẩn dụ tương tác (interaction metaphors)

- **Lợi ích — biểu tượng quen thuộc**: Các biểu tượng Resume/Pause (▶ / ❚❚) và biểu tượng cờ ca-rô của Finish mượn trực tiếp từ trình phát nhạc/video và đua xe — những lĩnh vực đã quen thuộc từ trước. Không cần học riêng gì về Strava để đọc hiểu chúng.

#### iv. Khả năng sử dụng (usability)

- **Khả năng học (Learnability)**: Cao. Toàn bộ vòng lặp ghi hoạt động cốt lõi được thao tác thành công ngay trong lần trải nghiệm đầu tiên, chưa từng tiếp xúc Strava trước đó, không hề do dự.
- **Hiệu suất (Efficiency)**: Tốt trong lúc ghi hoạt động — ít lần chạm cho Start/Pause/Resume — nhưng giảm mạnh ngay sau Finish, nơi bốn màn hình phụ, không được yêu cầu, đứng chắn giữa thời điểm nhấn Finish và thời điểm nhiệm vụ được xem là đã hoàn thành.
- **Lỗi (Errors)**: Không có lỗi nào trong phần ghi hoạt động.

### d. Các loại người dùng và bối cảnh khác nhau

#### i. Người mới bắt đầu

Tình huống này là một ví dụ trực tiếp của nhóm người mới bắt đầu: chưa từng tiếp xúc Strava trước đó, và vòng lặp cốt lõi được nắm bắt ngay trong lần thử đầu tiên mà không cần hướng dẫn nào.

#### ii. Người dùng có kinh nghiệm

Một người dùng có kinh nghiệm nhiều khả năng đã biết trước trình tự Finish → Save → Share do đã dùng nhiều lần, nên yếu tố bất ngờ nói trên sẽ giảm dần theo thời gian — nhưng số lần chạm thừa vẫn còn đó, nên chi phí về hiệu suất vẫn tồn tại kể cả khi sự bất ngờ đã biến mất.

#### iii. Người dùng lớn tuổi

Thanh nút Pause/Resume/Finish rộng có vùng chạm lớn, điều này nhìn chung giúp ích cho người có khả năng vận động tinh kém hơn hoặc thị lực yếu hơn. Đây là một điểm mạnh thiết kế đáng giữ lại bất kể ai dùng ứng dụng.

#### iv. Người dùng khuyết tật

Một người dùng phụ thuộc vào trình đọc màn hình sẽ hoàn toàn phụ thuộc vào khoảng trống phản hồi-chỉ-qua-thị-giác đã nói ở trên — không có xác nhận qua rung hay âm thanh, các thay đổi trạng thái (Paused, Resumed, Finished) sẽ không được thông báo qua kênh phi thị giác, trừ khi các nhãn dành cho trình đọc màn hình của ứng dụng xử lý việc này riêng. Đây là một rủi ro thực sự, vì thiết kế hiện tại chỉ dựa vào phản hồi thị giác.

#### v. Ràng buộc môi trường

Phiên ghi hoạt động diễn ra ngoài trời, ban ngày, với tín hiệu ổn định, nên chói nắng và trôi GPS không thực sự được quan sát thấy. Tuy vậy, hai điều kiện vẫn đáng lưu ý như rủi ro tiềm ẩn, vì chúng xuất phát trực tiếp từ cách màn hình và phương pháp theo dõi được xây dựng: màn hình ghi hoạt động dùng nền đen, dễ bị chói dưới ánh nắng trực tiếp hơn một nền sáng màu; và các con số quãng đường/tốc độ trực tiếp phụ thuộc hoàn toàn vào tín hiệu GPS, vốn thường yếu đi ở khu vực đô thị đông đúc với nhà cao tầng che khuất tầm nhìn vệ tinh.

### e. Đề xuất giải pháp dựa trên nguyên lý HCI

- **Vấn đề quan sát được**: Finish được theo sau bởi bốn màn hình không tùy chọn trước khi đạt trạng thái ổn định, phá vỡ kỳ vọng "Finish = xong."
  **Nguyên lý HCI liên quan**: Quy tắc vàng số 4 của Shneiderman ("thiết kế hộp thoại để tạo cảm giác khép lại") và Quy tắc vàng số 7 ("hỗ trợ quyền kiểm soát của người dùng").
  **Vì sao giải pháp này hiệu quả**: một điểm dừng rõ ràng ngay sau Finish khôi phục lại cảm giác khép lại đúng lúc được mong đợi, và cho phép lựa chọn có tiếp tục sang việc chia sẻ hay không, thay vì bị kéo vào đó.
  **Giải pháp**: ngay sau Finish, hiện một màn hình nhẹ nhàng duy nhất — "Activity saved. View it now, or share later?" (Đã lưu hoạt động. Xem ngay, hay chia sẻ sau?) — với hai nút rõ ràng. Chuyển cửa sổ thành tích và bảng Share vào phía sau một lựa chọn "chia sẻ sau" thay vì hiện tự động.

- **Vấn đề quan sát được**: Xác nhận Pause/Resume/Finish chỉ qua thị giác, buộc phải nhìn màn hình trong lúc đang đi bộ và quan sát đường.
  **Nguyên lý HCI liên quan**: phản hồi nên dùng kênh phù hợp với tình huống — thị giác, thính giác, hoặc xúc giác — và thiết kế nên giảm thiểu việc di chuyển mắt khi sự chú ý cần ở nơi khác.
  **Vì sao giải pháp này hiệu quả**: một cú rung ngắn có thể cảm nhận được mà không cần nhìn, nên có được xác nhận mà không phải rời mắt khỏi đường.
  **Giải pháp**: thêm một cú rung ngắn ở mỗi lần đổi trạng thái (Start, Pause, Resume, Finish), để có thể xác nhận thao tác đã thành công mà không cần liếc xuống.

---

## 3. Tình huống sử dụng 2: Xem lại số liệu sau khi hoàn thành hoạt động

### a. Phân tích tình huống sử dụng 2

**Mục tiêu**: hiểu hoạt động vừa hoàn thành diễn ra thế nào — quãng đường, tốc độ, độ cao, các chặng (splits).
**Tác nhân kích hoạt**: mở hoạt động đã lưu và cuộn qua các màn hình chi tiết và phân tích của nó.
**Các màn hình quan sát được**:
- Màn hình chi tiết hoạt động (quãng đường, thời gian di chuyển, độ cao đạt được).
![Activity detail screen](strava-images/IMG_0521.PNG)
*IMG_0521 — Màn hình chi tiết hoạt động: Distance/Moving Time/Elevation Gain cùng biểu ngữ Kudos.*
- Màn hình Workout Analysis (các chặng, bản đồ bay lượn flyover).
![Workout Analysis screen](strava-images/IMG_0525.PNG)
*IMG_0525 — Màn hình Workout Analysis: danh sách Laps và bản đồ Flyover.*
- Biểu đồ độ cao.
![Elevation chart](strava-images/IMG_0526.PNG)
*IMG_0526 — Biểu đồ độ cao: Elevation Gain và Max Elevation.*
- Màn hình biểu đồ tốc độ / số liệu (Avg Pace, Moving Time, Avg Elapsed Pace, Elapsed Time, Fastest Split).
![Pace chart screen](strava-images/IMG_0527.PNG)
*IMG_0527 — Màn hình biểu đồ tốc độ: Avg Pace/Moving Time/Avg Elapsed Pace/Elapsed Time/Fastest Split.*

### b. Bối cảnh và cách người dùng tương tác với tình huống này qua giao diện

#### i. Bối cảnh 1

- **Ở đâu / Khi nào / Tình huống người dùng**: Việc xem lại này diễn ra trong cùng phiên thử nghiệm với buổi đi bộ đã ghi, xem lại hoạt động đã lưu trên cùng chiếc iPhone.
- **Cách tương tác**: Cuộn và chạm qua một màn hình số liệu một cột.
- **Kết quả mong đợi**: Hiểu nhanh buổi hoạt động diễn ra thế nào bằng cách đọc các con số hiển thị.

### c. Áp dụng nguyên lý HCI (Lợi ích & Hạn chế)

#### i. Khả năng con người

- **Lợi ích — chunking (gom nhóm thông tin)**: Dữ liệu được hiển thị dưới dạng các khối số liệu lớn và biểu đồ (độ cao, tốc độ) thay vì bảng dày đặc. Gom nhóm các con số theo cách này, thay vì liệt kê dài dòng, giảm bớt lượng mắt phải quét và não phải giữ lại cùng lúc.
- **Hạn chế**: Một số chỉ số có tên gần giống nhau nằm sát cạnh nhau mà không có nhãn giải thích điều gì phân biệt chúng — mô tả cụ thể ở dưới.

#### ii. Mô hình tư duy của người dùng

- **Hạn chế — nhớ lại thay vì nhận diện**: Avg Pace, Avg Elapsed Pace, Moving Time, và Elapsed Time đều được hiển thị mà không có gợi ý trực quan nào giải thích điều gì phân biệt chúng. Nhận diện (recognition) nghĩa là hiểu một điều gì đó vì có gợi ý trực quan ngay trước mắt; nhớ lại (recall) nghĩa là phải tự nhớ ý nghĩa mà không có gợi ý nào cả — và nhận diện luôn dễ hơn. Ở đây các nhãn buộc phải nhớ lại thay vì nhận diện: các chỉ số như Avg Elapsed Time, Elapsed Time, và Fastest Split không thể hiện rõ mục đích sử dụng của chúng chỉ qua tên gọi, khiến ý nghĩa của chúng không rõ ràng ngay từ lần nhìn đầu tiên.
- **Hạn chế — thuật ngữ gần giống nhau gây rối**: "Elapsed Pace" nằm cạnh "Pace," và "Elapsed Time" nằm cạnh "Moving Time," đọc lên giống như thuật ngữ khó phân biệt hơn là ngôn ngữ đơn giản có thể nhận ra ngay từ cái nhìn đầu tiên. Ngôn ngữ giao diện tốt nên dùng từ ngữ mà một người dùng bình thường đã hiểu sẵn, chứ không phải các thuật ngữ kỹ thuật gần giống hệt nhau.

#### iii. Ẩn dụ tương tác

Biểu đồ độ cao và tốc độ dùng quy ước biểu đồ đường/vùng tiêu chuẩn từ trực quan hóa dữ liệu thông thường — không có vấn đề ẩn dụ riêng của Strava được quan sát thấy trên màn hình này.

#### iv. Khả năng sử dụng

- **Khả năng học (Learnability)**: Thấp, cụ thể cho màn hình này: một số nhãn chỉ số không thể phân biệt được nếu không có trợ giúp bên ngoài, điều này đi ngược lại mục tiêu khả dụng cơ bản — một giao diện mới nên có thể được hiểu ngay mà không cần được dạy trước.
- **Lỗi (Errors)**: Không có lỗi nào xảy ra trực tiếp, vì đây là màn hình chỉ đọc. Nhưng sự nhầm lẫn về nhãn tạo ra một rủi ro thực sự: người dùng có thể dễ dàng nhầm lẫn Moving Time (thời gian thực sự di chuyển) với Elapsed Time (tổng thời gian bao gồm cả lúc dừng) khi so sánh các buổi chạy của chính họ theo thời gian.

### d. Các loại người dùng và bối cảnh khác nhau

#### i. Người mới bắt đầu

Đây là một ví dụ trực tiếp của nhóm người mới bắt đầu: sự nhầm lẫn này xảy ra ngay trong lần đầu tiếp cận màn hình này.

#### ii. Người dùng có kinh nghiệm

Một người dùng đến từ ứng dụng theo dõi thể chất khác nhiều khả năng đã biết sẵn sự khác biệt giữa "moving time" và "elapsed time," vì cặp thuật ngữ này phổ biến trong cả nhóm ứng dụng thể chất — nghĩa là cặp nhãn cụ thể này gây ít khó khăn hơn cho họ, dù cách dùng từ gần giống nhau "Pace" so với "Elapsed Pace" là riêng của Strava và vẫn sẽ mới lạ với hầu hết người dùng bất kể kinh nghiệm.

### e. Đề xuất giải pháp dựa trên nguyên lý HCI

- **Vấn đề quan sát được**: không thể phân biệt được Avg Pace / Avg Elapsed Pace / Moving Time / Elapsed Time trên màn hình biểu đồ tốc độ.
  **Nguyên lý HCI liên quan**: ưu tiên nhận diện hơn nhớ lại, và dùng ngôn ngữ đơn giản thay vì thuật ngữ gần giống nhau khó phân biệt.
  **Vì sao giải pháp này hiệu quả**: đặt lời giải thích ngay tại nơi người dùng đang nhìn biến một việc phải đoán thành một việc chỉ cần nhận diện — không cần ghi nhớ.
  **Giải pháp**: thêm một biểu tượng thông tin nhỏ cạnh mỗi nhãn trong bốn nhãn này, hiện một định nghĩa một dòng khi chạm vào (ví dụ: "Elapsed Time: tổng thời gian bao gồm cả lúc dừng. Moving Time: thời gian thực sự di chuyển."). Hiện tự động lần đầu tiên người dùng mở màn hình này, sau đó cho phép bỏ qua ở các lần xem sau.

---

## 4. Tình huống sử dụng 3: Khám phá Groups — Thử thách & Câu lạc bộ

### a. Phân tích tình huống sử dụng 3

**Mục tiêu**: khám phá những gì tab Groups cung cấp qua các tab con Active, Challenges, và Clubs. Với Active và Challenges, đây là sự tò mò tự nhiên chứ không phải nhu cầu thực sự ngay từ đầu. Riêng với Clubs, có một mục tiêu rõ ràng đặt ra từ đầu: tìm một câu lạc bộ chạy bộ đang hoạt động ở khu vực.
**Tác nhân kích hoạt**: chạm tab Groups từ thanh điều hướng dưới.
**Các bước quan sát được**:
1. Tab Groups Active ("Design Your Own Challenge" khóa trả phí cùng thanh tiến độ của các thử thách đã tham gia).
![Groups Active tab](strava-images/IMG_0532.PNG)
*IMG_0532 — Tab Groups Active: khóa trả phí Design Your Own Challenge và thanh tiến độ thử thách đã tham gia.*
2. Tab Challenges, thẻ có nút Join ("July 5K Challenge" card, nút Join, danh sách "Recommended For You").
![Challenges tab, Join button](strava-images/IMG_0533.PNG)
*IMG_0533 — Tab Challenges: thẻ July 5K Challenge với nút Join và danh sách Recommended For You.*
3. Chạm Join trên thẻ thử thách → nút đổi trạng thái, nhưng màn hình không đổi.
4. Tab Clubs / màn hình khám phá câu lạc bộ (quảng cáo "Create Your Own Strava Club", biểu ngữ "The Strava Club").
![Clubs tab](strava-images/IMG_0534.PNG)
*IMG_0534 — Tab Clubs: quảng cáo Create Your Own Strava Club và biểu ngữ The Strava Club.*

### b. Bối cảnh và cách người dùng tương tác với tình huống này qua giao diện

#### i. Bối cảnh 1

- **Ở đâu / Khi nào**: Một phiên riêng biệt so với buổi đi bộ đã ghi.
- **Tình huống người dùng**: Chủ động khám phá các tính năng của ứng dụng thay vì xử lý một nhiệm vụ gấp. Với Active/Challenges, mục đích ban đầu chỉ là tò mò; với Clubs, có một mục tiêu thực sự — tìm một câu lạc bộ chạy bộ gần nhà.
- **Cách tương tác**: Sự chú ý đi thẳng đến yếu tố nổi bật nhất về mặt thị giác trên mỗi thẻ — nút Join — và cú chạm xảy ra trực tiếp lên nút đó mà không đọc nhãn trước. Quan sát cho thấy: khi nhìn thấy một thẻ câu lạc bộ hay thẻ thử thách, sự chú ý tập trung vào nút và cú chạm xảy ra ngay mà không đọc chữ "join", kèm theo giả định rằng cần chạm vào mới mở được trang chi tiết của thử thách.
- **Kết quả mong đợi**: Chạm Join được kỳ vọng sẽ mở ra một trang chi tiết cho thử thách. Với Clubs, mục tiêu là tìm một câu lạc bộ chạy bộ đang hoạt động gần khu vực đang chạy.

### c. Áp dụng nguyên lý HCI (Lợi ích & Hạn chế)

#### i. Khả năng con người

- **Hạn chế — một nút sáng màu kéo mắt trước khi thẻ được đọc**: Như đã quan sát ở trên, sự chú ý tập trung vào nút Join và cú chạm xảy ra trước khi phần còn lại của thẻ kịp được đọc. Kiểu dáng nút Join màu cam sáng, hành động chính, là độ tương phản màu mạnh nhất trên thẻ. Vùng nhìn chi tiết của mắt (fovea) chỉ bao phủ một vùng trung tâm nhỏ; mọi thứ ngoài điểm đó được tiếp nhận qua thị giác ngoại vi, vốn phản ứng với chuyển động và độ tương phản mạnh hơn là chi tiết. Một nút tương phản cao hoạt động như một tín hiệu thu hút sự chú ý kiểu đó — nó kéo mắt, và cú chạm, về phía nó trước, trước khi phần còn lại của thẻ được đọc.

#### ii. Mô hình tư duy của người dùng

- **Hạn chế — giao diện làm ngược lại điều được kỳ vọng**: Mô hình tư duy hình thành tự nhiên khi nhìn thẻ là "chạm vào yếu tố nổi bật trên một thẻ sẽ dẫn đến thêm chi tiết." Hành vi thực tế của giao diện lại là "chạm Join, và chỉ trạng thái của chính nút đó thay đổi — không có gì khác xảy ra." Trải nghiệm thực tế phản ánh rõ sự lệch pha này: sau cú chạm, không có gì xảy ra ngoài việc nút đổi trạng thái, trong khi điều được mong đợi là chuyển sang xem thêm chi tiết; nỗ lực tìm khung xem chi tiết bằng cách tiếp tục tập trung vào nút — thay vì đọc hay suy xét chức năng thực sự của nút — dẫn đến bế tắc, không tìm ra được đường vào trang chi tiết. Đây là một sự lệch pha chính xác giữa điều một cú chạm được kỳ vọng sẽ làm và điều nó thực sự làm — không phải một nhận xét mơ hồ về một thẻ gây rối.

#### iii. Ẩn dụ tương tác

- **Hạn chế — hai hành động khác nhau trông như một**: Join (chỉ đổi trạng thái) và "mở chi tiết" (nên điều hướng đến đâu đó) nằm trên cùng một thẻ mà không có ranh giới trực quan nào giữa chúng. Những thứ giống nhau nên trông và hoạt động giống nhau, và những thứ khác nhau nên trông khác biệt rõ ràng — ở đây, hai thao tác khác nhau dùng chung một bề mặt mà không có sự phân biệt nào cả.

#### iv. Khả năng sử dụng

- **Khả năng học (Learnability)**: Thấp — khung xem chi tiết không bao giờ được tìm ra trong suốt phiên trải nghiệm này, dù đã chạm qua nhiều thẻ thử thách và câu lạc bộ.
- **Phản hồi / Khả năng nhìn thấy (Feedback / Visibility)**: Việc đổi nhãn của nút là đủ phản hồi cho chính thao tác chuyển đổi Join. Nhưng với hành động riêng biệt là xem chi tiết, giao diện không đưa ra phản hồi hay khả năng nhìn thấy nào cả — hành động đó xem như không tồn tại trên màn hình.
- **Sự hài lòng (Satisfaction)**: Sự lệch pha này không gây khó chịu đáng kể trong bối cảnh đang chủ động khám phá tính năng chứ không theo đuổi một nhiệm vụ gấp — mức độ ảnh hưởng thấp một phần vì mục đích ban đầu chỉ là thử nghiệm. Tuy nhiên, trong một tình huống có mục tiêu thực sự và cấp bách hơn — chẳng hạn thực sự muốn tham gia một thử thách cụ thể ngay lúc đó — cùng một khoảng trống phản hồi này nhiều khả năng sẽ gây khó chịu rõ rệt hơn, vì không có cách nào để biết cú chạm có đạt được điều mong muốn hay không.

**Riêng với Clubs**: mục tiêu thực sự đặt ra ban đầu — tìm một câu lạc bộ chạy bộ đang hoạt động gần khu vực — không đạt được khi kết thúc phiên khám phá tab này; không có cảm giác hoàn thành nào đọng lại. Thay vào đó, màn hình chỉ hiện một quảng cáo chung chung "Create Your Own Strava Club" và "The Strava Club" (câu lạc bộ chính thức của Strava), không có tính năng khám phá câu lạc bộ theo vị trí hay theo hoạt động nào hiển thị ở bất kỳ đâu trên tab. Một nhiệm vụ như "tìm câu lạc bộ gần tôi" cần có một điểm truy cập rõ ràng riêng trên màn hình; ở đây không có, nên mục tiêu thực sự đặt ra ban đầu không có nơi nào để đi.

### d. Các loại người dùng và bối cảnh khác nhau

#### i. Người mới bắt đầu

Tình huống này là một ví dụ trực tiếp của nhóm người mới bắt đầu — đây là lần tiếp xúc đầu tiên với Groups, Challenges, và Clubs.

#### ii. Người dùng có kinh nghiệm

Một người dùng đã quen thuộc với các ứng dụng mạng xã hội dạng thẻ (ứng dụng sự kiện, ứng dụng liệt kê nhóm) có thể đã kỳ vọng sẵn một quy ước rằng chạm vào thân thẻ sẽ mở chi tiết còn một nút riêng, nhỏ hơn thì thực hiện thao tác nhanh — nghĩa là cùng một sự lệch pha vẫn có thể khiến họ vấp phải, vì các thẻ của Strava hoàn toàn không tách biệt hai hành động đó.

### e. Đề xuất giải pháp dựa trên nguyên lý HCI

- **Vấn đề quan sát được**: Join và "mở chi tiết" dùng chung một vùng chạm trên thẻ mà không có sự phân biệt trực quan nào.
  **Nguyên lý HCI liên quan**: những thứ giống nhau nên hoạt động giống nhau, và những thứ khác nhau nên trông khác biệt (tính nhất quán và khả năng gợi ý - affordance).
  **Vì sao giải pháp này hiệu quả**: cho mỗi hành động một yếu tố trực quan riêng biệt cho người dùng biết chính xác mỗi cú chạm sẽ làm gì, trước khi họ chạm vào.
  **Giải pháp**: làm cho thân thẻ có thể chạm để mở chi tiết, và thu nhỏ nút Join thành một điều khiển nhỏ hơn, tách biệt rõ ràng — ví dụ, một biểu tượng mũi tên (chevron) trên thẻ để báo hiệu "thêm chi tiết," cạnh một nút Join có kiểu dáng khác biệt rõ ràng.

- **Vấn đề quan sát được**: sau khi chạm Join, phản hồi duy nhất là việc đổi nhãn của chính nút đó — hành động "xem chi tiết" không có phản hồi hay khả năng nhìn thấy ở bất kỳ đâu.
  **Nguyên lý HCI liên quan**: các hành động nên đưa ra phản hồi tức thì, đầy đủ thông tin, và mọi thao tác trên màn hình nên có thể nhìn thấy được đối với người dùng.
  **Vì sao giải pháp này hiệu quả**: kết hợp xác nhận đổi trạng thái với một bước tiếp theo trực tiếp cho người dùng biết cả rằng cú chạm của họ đã thành công lẫn việc cần làm tiếp theo.
  **Giải pháp**: sau khi Join, hiện một xác nhận ngắn kèm liên kết trực tiếp — ví dụ, "Joined! Tap here to see challenge details." (Đã tham gia! Chạm vào đây để xem chi tiết thử thách.)

- **Vấn đề quan sát được**: mục tiêu thực sự đặt ra ban đầu — tìm một câu lạc bộ gần nhà — không có điểm truy cập nào hiển thị ở bất kỳ đâu trên tab Clubs.
  **Nguyên lý HCI liên quan**: một màn hình nên có một tính năng rõ ràng đằng sau mỗi mục tiêu phổ biến của người dùng mà nó nhắm đến hỗ trợ.
  **Vì sao giải pháp này hiệu quả**: thêm một điểm truy cập trực tiếp biến một mục tiêu mà giao diện hiện đang bỏ qua thành một mục tiêu mà nó chủ động hỗ trợ.
  **Giải pháp**: thêm một ô tìm kiếm hoặc bộ lọc "Find a club near you" (Tìm câu lạc bộ gần bạn) trực tiếp trên màn hình chính của tab Clubs, thay vì chỉ hiện "Create your own club" và câu lạc bộ chính thức duy nhất của Strava.

---

## Ghi chú về Phạm vi và Bằng chứng

Báo cáo này chỉ bao gồm Sản phẩm 1 (Strava). Sản phẩm 2 là trách nhiệm riêng của một thành viên khác trong nhóm. Các tình huống sử dụng ở trên giới hạn trong những luồng thao tác được dự án này trải nghiệm trực tiếp trong lần đầu sử dụng ứng dụng, có ảnh chụp màn hình tương ứng: ghi lại và lưu một buổi đi bộ, xem lại số liệu của nó, và duyệt qua tab Groups. Các màn hình khác được chụp trong cùng phiên — tab Maps, và các tab con Workouts và Settings của tab You — đã được xem nhưng không được viết thành tình huống sử dụng đầy đủ trong báo cáo này, nên chúng được bỏ qua thay vì viết dựa trên phỏng đoán.

Lý luận HCI trong phần "Áp dụng nguyên lý HCI" và "Đề xuất giải pháp dựa trên nguyên lý HCI" của mỗi tình huống sử dụng dựa trên ba nguồn từ khóa học: khả năng con người và các khía cạnh khả dụng (kênh phản hồi, khả năng nhìn thấy, khả năng gợi ý, tính nhất quán, nhận diện so với nhớ lại, mô hình tư duy, mô hình khái niệm, ẩn dụ giao diện, chunking, và các mục tiêu khả dụng), Tám Quy tắc vàng của Shneiderman và quy trình thiết kế UI (khép lại hộp thoại, ngăn ngừa lỗi, phản hồi đầy đủ thông tin, quyền kiểm soát của người dùng), và phân tích nhiệm vụ (nắm bắt mục tiêu của một nhiệm vụ, môi trường của nó, và cách nó được học).
