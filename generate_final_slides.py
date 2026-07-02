import json

slides = [
    {
        "uc": "",
        "title": "STRAVA — Product Research & Interaction Analysis",
        "content": """
            <ul>
                <li>CSC13112 · UI/UX Design · Project Assignment 1 (PA1)</li>
                <li>Group 03 — FIT-HCMUS</li>
                <li><em>Presenter:</em> [Your Name / Student ID]</li>
            </ul>
        """,
        "image": "strava-images/IMG_0521.PNG",
        "image_class": "phone background-blur",
        "notes": "Chào mọi người. Khác với cách tiếp cận lý thuyết thông thường, bài phân tích này sẽ tập trung vào những trải nghiệm thực tế, những cú vấp ngã (friction) và cảm nhận cá nhân của một người dùng mới tinh khi lần đầu tiên trải nghiệm Strava ngoài đời thực."
    },
    {
        "uc": "",
        "title": "Product & User Profile",
        "content": """
            <ul>
                <li><strong>What is Strava:</strong> Multi-sport GPS tracker + social ecosystem (Record → Analyze → Share).</li>
                <li><strong>Core User Goal:</strong> Record outdoor activities & review basic metrics.</li>
                <li><strong>Primary Audience:</strong> Health-focused active individuals (93% non-competitive).</li>
                <li><strong>Secondary Segments:</strong> Walkers, cyclists, multi-sport, Gen Z.</li>
                <li><strong>Evaluation Scope:</strong> iOS (iPhone), Free Tier, First-Time User Experience.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0521.PNG",
        "image_class": "phone",
        "notes": "Strava định vị họ là mạng xã hội thể thao. Nhưng với mình, một người dùng đi bộ bình thường, nhu cầu duy nhất của mình chỉ là bật app lên, ghi lại quãng đường và xem thời gian. Sự chênh lệch giữa định hướng của hệ thống (muốn bạn chia sẻ, thi đấu) và nhu cầu thực tế của mình (chỉ muốn tracking cơ bản) chính là nguồn gốc của hầu hết các vấn đề UI/UX trong bài báo cáo này."
    },
    {
        "uc": "",
        "title": "Core Use Cases Index",
        "content": """
            <ul>
                <li><strong>Use Case 1:</strong> Recording, Finishing, and Saving an Outdoor Walk (Core Loop).</li>
                <li><strong>Use Case 2:</strong> Reviewing Post-Activity Statistical Performance Metrics.</li>
                <li><strong>Use Case 3:</strong> Exploring Regional Routes and Segments (Maps).</li>
                <li><strong>Use Case 4:</strong> Engaging with Community (Challenges & Clubs).</li>
            </ul>
        """,
        "image": "",
        "notes": "Mình sẽ đi qua 4 luồng chính: Ghi lại hoạt động, Xem lại thống kê, Khám phá bản đồ, và Tìm kiếm hội nhóm. Ở mỗi luồng, mình không chỉ đánh giá theo các tiêu chí HCI mà còn đào sâu vào nguyên nhân tâm lý vì sao một thiết kế lại gây khó chịu."
    },
    # UC1
    {
        "uc": "Use Case 1",
        "title": "Overview: Record, Finish, and Save",
        "content": """
            <ul>
                <li><strong>Goal:</strong> Capture precise GPS data in real-time and save it.</li>
                <li><strong>The Core Loop:</strong> Start → Pause → Resume → Finish.</li>
                <li><strong>Live Interface Displays:</strong> Tracking map view + numeric telemetry (Duration, Distance, Speed).</li>
            </ul>
        """,
        "image": "strava-images/IMG_0514.PNG",
        "image_class": "phone highlight-solution",
        "notes": "Luồng đầu tiên: Ghi lại một cuốc đi bộ. Tính năng này Strava làm rất tốt ở bề mặt. Mọi thứ to, rõ ràng."
    },
    {
        "uc": "Use Case 1",
        "title": "User Interaction Context",
        "content": """
            <ul>
                <li><strong>During Active Recording (Outdoors):</strong>
                    <ul>
                        <li>Urban street, early morning sunlight (~06:09 AM), screen glare.</li>
                        <li>Walking motion, attention divided between path and screen.</li>
                        <li>One-handed touch, quick downward glances.</li>
                    </ul>
                </li>
                <li><strong>At Workflow Termination:</strong>
                    <ul>
                        <li>Stationary. Tap "Finish" expecting task to end.</li>
                        <li>Implicit Expectation: Direct access to saved record.</li>
                    </ul>
                </li>
            </ul>
        """,
        "image": "strava-images/IMG_0515.PNG",
        "image_class": "phone",
        "notes": "Nhưng phải đặt vào bối cảnh thực tế: Mình đang đi bộ ngoài đường, trời hửng sáng, cầm điện thoại một tay. Mình chỉ có thể liếc nhìn màn hình chớp nhoáng. Và khi kết thúc, mình đang đứng thở dốc trên vỉa hè, chỉ muốn cất điện thoại đi."
    },
    {
        "uc": "Use Case 1",
        "title": "Use Case Interactions",
        "content": """
            <ul>
                <li><strong>Step 1:</strong> Tap "Record" icon on navigation bar.</li>
                <li><strong>Step 2:</strong> Tap "Start" to initialize GPS.</li>
                <li><strong>Step 3:</strong> Tap large "Pause" to halt tracking.</li>
                <li><strong>Step 4:</strong> Hold/press "Finish" flag icon.</li>
                <li><strong>Step 5:</strong> Scroll through extensive secondary metadata form.</li>
            </ul>
        """,
        "image": "",
        "notes": "Các thao tác Start, Pause, Finish rất đơn giản. Tuy nhiên, rắc rối bắt đầu ngay sau cú chạm vào nút Finish. Thay vì kết thúc, app ném vào mặt mình một cái form dài thòng để điền thông tin."
    },
    {
        "uc": "Use Case 1",
        "title": "Human Capabilities Matrix",
        "content": """
            <div class="grid-2x2">
                <div class="card">
                    <h4>Vision & Attention</h4>
                    <p class="benefit">Benefit: Large telemetry values optimize foveal vision.</p>
                    <p class="drawback highlight-text">Drawback: Dark-mode UI enhances glare outdoors.</p>
                </div>
                <div class="card">
                    <h4>Touch & Motor</h4>
                    <p class="benefit">Benefit: Wide buttons suit single-handed use.</p>
                </div>
                <div class="card">
                    <h4>Audio & Haptic Feedback</h4>
                    <p class="drawback highlight-text">Drawback: Zero haptic/audio confirmation. Forces visual verification on active roads.</p>
                </div>
                <div class="card">
                    <h4>Memory & Cognition</h4>
                    <p class="benefit">Benefit: Matches stopwatch concepts.</p>
                    <p class="drawback">Drawback: Post-workout sequence forces high cognitive load.</p>
                </div>
            </div>
        """,
        "image": "",
        "notes": "Phân tích dưới góc độ năng lực con người: Số hiển thị to rất tốt cho thị giác foveal. NHƯNG điểm trừ chí mạng ở đây là app KHÔNG CÓ rung (haptic). Khi đang đi bộ, mắt bận nhìn đường, mình bấm Pause và không biết nó ăn chưa, lại phải cúi xuống nhìn chằm chằm màn hình. Đây là lỗi thiết kế ảnh hưởng trực tiếp đến sự an toàn."
    },
    {
        "uc": "Use Case 1",
        "title": "User Mental Model Analysis",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>The Operational Breakpoint:</strong> System forces 5 modal screens before home dashboard (Save Form → "Nice Work!" → Achievement → Share Sheet).</li>
                <li class="drawback"><strong>HCI Breach:</strong> Violates Golden Rule #4 (Design dialogs to yield closure).</li>
            </ul>
            <blockquote>"What felt a bit different to me is that after I press Finish on a walk, it shows a screen to share... that felt strange."</blockquote>
        """,
        "image": "strava-images/IMG_0522.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Về mặt nhận thức, đây là sự phản bội kỳ vọng. Mình bấm Finish tức là 'xong rồi'. Nhưng hệ thống ép mình qua 5 màn hình phụ: từ form lưu, chúc mừng, khoe thành tích, đến tự động bật cả bảng Share. Việc này phá vỡ cảm giác hoàn thành (closure). Hệ thống ưu tiên sự viral của app thay vì sự thoải mái của người dùng."
    },
    {
        "uc": "Use Case 1",
        "title": "Interaction Metaphors",
        "content": """
            <ul>
                <li class="benefit"><strong>Media Player Schemas:</strong> ▶ (Resume), ❚❚ (Pause) draw on universal standards.</li>
                <li class="benefit"><strong>Athletic Schemas:</strong> Checkered flag (🏁) directly links to crossing a finish line.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0515.PNG",
        "image_class": "phone highlight-solution",
        "notes": "Về mặt ẩn dụ, Strava làm rất tốt. Nút play, pause hay cờ đích là những ngôn ngữ quốc tế. Không cần học cũng biết xài."
    },
    {
        "uc": "Use Case 1",
        "title": "Usability Diagnostic",
        "content": """
            <ul>
                <li><strong>Learnability:</strong> Exceptionally High.</li>
                <li><strong>Efficiency:</strong> Polarized. High during tracking; steeply declines post-finish due to unwanted social screens.</li>
                <li><strong>Memorability:</strong> High retention (standard icons).</li>
                <li><strong>Error Recovery:</strong> Poor post-finish (no obvious shortcut to bypass the forced sharing flow).</li>
            </ul>
        """,
        "image": "",
        "notes": "Tính sử dụng (usability) có sự phân cực rõ rệt. Rất dễ học và hiệu quả lúc đang đi. Nhưng ngay khi bấm Finish, hiệu quả rớt thê thảm vì mình phải tốn quá nhiều thao tác (tap) để thoát khỏi những màn hình không mong muốn."
    },
    {
        "uc": "Use Case 1",
        "title": "Different User Types & Contexts",
        "content": """
            <ul>
                <li><strong>Beginners:</strong> Intuitive core loop, but immediate confusion at post-finish social loop.</li>
                <li><strong>Experienced:</strong> Unnecessary multi-tap tax remains an ongoing friction point.</li>
                <li><strong>Elderly:</strong> Large targets help, but small typography on save form hinders.</li>
                <li><strong>Disabilities:</strong> Visual-only feedback poses a high barrier for screen-reader users.</li>
            </ul>
        """,
        "image": "",
        "notes": "Với người mù hoặc người cao tuổi, việc thiếu phản hồi rung và chữ nhỏ trong form lưu là một rào cản lớn. Còn với người bình thường, cái 'thuế thao tác' (multi-tap tax) để thoát khỏi màn hình Share vẫn là thứ gây ức chế dài hạn."
    },
    {
        "uc": "Use Case 1",
        "title": "Proposed HCI Solutions",
        "content": """
            <ul>
                <li><strong>Solution A: Streamlined Task Closure</strong>
                    <br>Explicit confirmation hub: <em>"Activity Saved. View Now | Share Later"</em>. Restores Golden Rule #4 & #7 (Internal locus of control).</li>
                <li><strong>Solution B: Multi-Channel State Feedback</strong>
                    <br>Integrate short haptic vibration pulses on every major state transition (Start, Pause, Resume, Finish).</li>
            </ul>
        """,
        "image": "",
        "notes": "Giải pháp dưới góc độ critical thinking: Không cần đập đi xây lại. Chỉ cần 2 thay đổi nhỏ: 1. Trả lại quyền kiểm soát (locus of control) bằng một nút 'Share Later' đơn giản thay vì ép buộc. 2. Thêm một cái rung nhẹ (haptic) để giải phóng đôi mắt người dùng khỏi màn hình."
    },
    # UC2
    {
        "uc": "Use Case 2",
        "title": "Overview: Reviewing Post-Activity Stats",
        "content": """
            <ul>
                <li><strong>Goal:</strong> Comprehend workout performance data.</li>
                <li><strong>Layers:</strong> Overview → Analytics View → Elevation Charts → Pace/Split Breakdowns.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0521.PNG",
        "image_class": "phone",
        "notes": "Luồng thứ 2: Đi xong rồi thì mở ra xem mình được bao nhiêu km, tốc độ bao nhiêu."
    },
    {
        "uc": "Use Case 2",
        "title": "User Interaction Context",
        "content": """
            <ul>
                <li><strong>Environmental State:</strong> Settled indoor, seated.</li>
                <li><strong>User Attention:</strong> High focal attention, low real-time risk.</li>
                <li><strong>Interaction Method:</strong> Vertical scrolling & single-tap on dense numeric arrays.</li>
                <li><strong>Implicit Goal:</strong> Quickly interpret data without needing to search for definitions.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0525.PNG",
        "image_class": "phone",
        "notes": "Lúc này bối cảnh thay đổi: mình đang ngồi nghỉ, rảnh rỗi lướt màn hình. Mình kỳ vọng sẽ đọc hiểu các chỉ số ngay lập tức mà không cần phải đi tra từ điển."
    },
    {
        "uc": "Use Case 2",
        "title": "Use Case Interactions",
        "content": """
            <ul>
                <li><strong>Step 1:</strong> Open activity log.</li>
                <li><strong>Step 2:</strong> Scroll top-level aggregated data cards.</li>
                <li><strong>Step 3:</strong> Tap sub-analysis panels (Laps, Chart Overlays).</li>
                <li><strong>Step 4:</strong> Horizontal drag along chart lines.</li>
            </ul>
        """,
        "image": "",
        "notes": "Mình lướt từ trên xuống dưới, bấm vào biểu đồ để xem chi tiết. Nhìn chung luồng thao tác không có gì phức tạp."
    },
    {
        "uc": "Use Case 2",
        "title": "Human Capabilities Matrix",
        "content": """
            <div class="grid-2x2">
                <div class="card">
                    <h4>Vision & Attention</h4>
                    <p class="benefit">Benefit: Neatly isolated data blocks prevent visual clutter.</p>
                </div>
                <div class="card">
                    <h4>Touch & Motor</h4>
                    <p class="drawback">Drawback: Interactive chart paths require high-precision horizontal dragging.</p>
                </div>
                <div class="card">
                    <h4>Audio & Haptic Feedback</h4>
                    <p><em>Not a primary channel.</em></p>
                </div>
                <div class="card">
                    <h4>Memory & Cognition</h4>
                    <p class="benefit">Benefit: "Chunking" design lowers cognitive overhead.</p>
                    <p class="drawback highlight-text">Drawback: Lack of clear inline definitions forces active recall.</p>
                </div>
            </div>
        """,
        "image": "",
        "notes": "Giao diện được gom nhóm (chunking) rất sạch sẽ. Nhưng điểm gãy về mặt nhận thức (Cognition) xuất hiện khi app ném cho mình một đống thuật ngữ chuyên ngành."
    },
    {
        "uc": "Use Case 2",
        "title": "User Mental Model Analysis",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>Recognition vs. Recall Failure:</strong> Similarly-named metrics (Average Pace, Average Elapsed Pace, Moving Time, Elapsed Time) lack visible cues.</li>
                <li class="drawback"><strong>Cognitive Mismatch:</strong> Forces <em>recall</em> over <em>recognition</em>. Prioritizes raw database labels over plain language.</li>
            </ul>
            <blockquote>"Things like Avg Elapsed Time, Elapsed Time... I don't understand what they're for."</blockquote>
        """,
        "image": "strava-images/IMG_0527.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Sự thất bại về thiết kế mental model: Strava lấy nguyên các biến trong cơ sở dữ liệu (Database labels) quăng ra giao diện người dùng. 'Elapsed Time' vs 'Moving Time' - không có một lời giải thích nào. Nó bắt người dùng phải nhớ (recall) thay vì nhận diện (recognition). Đây là sự vô tâm trong thiết kế nội dung (UX Writing)."
    },
    {
        "uc": "Use Case 2",
        "title": "Interaction Metaphors",
        "content": """
            <ul>
                <li class="benefit"><strong>Data Visualization Standards:</strong> Standard line and area charts.</li>
                <li><strong>Evaluation:</strong> High usability match. Intuitive reading based on everyday web graphics.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0526.PNG",
        "image_class": "phone",
        "notes": "Riêng phần biểu đồ thì làm rất tốt, tuân thủ đúng các tiêu chuẩn hiển thị dữ liệu (Data Viz) phổ biến nên rất dễ hiểu."
    },
    {
        "uc": "Use Case 2",
        "title": "Usability Diagnostic",
        "content": """
            <ul>
                <li><strong>Learnability:</strong> Low. Cannot distinguish terms without external lookups.</li>
                <li><strong>Efficiency:</strong> Weak. Ambiguous labels slow down data interpretation.</li>
                <li><strong>Memorability:</strong> Low/Moderate. High cognitive effort required to remember terms between sessions.</li>
                <li><strong>Error Recovery:</strong> High risk of misinterpreting total elapsed duration for active moving time.</li>
            </ul>
        """,
        "image": "",
        "notes": "Rõ ràng tính dễ học (Learnability) cực thấp. Mình không thể nào tự suy luận ra được, phải lên Google gõ 'Elapsed time strava là gì'. Nó làm giảm hiệu quả đọc hiểu và rất dễ gây hiểu nhầm dữ liệu cá nhân."
    },
    {
        "uc": "Use Case 2",
        "title": "Different User Types & Contexts",
        "content": """
            <ul>
                <li><strong>Beginners:</strong> Immediate confusion due to fitness jargon.</li>
                <li><strong>Experienced Athletes:</strong> Parse easily as they match standard terms (Garmin, Zwift).</li>
                <li><strong>Elderly:</strong> Small typography within dense sub-charts can make reading difficult.</li>
            </ul>
        """,
        "image": "",
        "notes": "Với dân chạy bộ chuyên nghiệp quen xài Garmin, họ sẽ thấy bình thường vì họ đã bị 'huấn luyện' bởi hệ sinh thái đó. Nhưng với 93% người dùng vì sức khoẻ (health-focused) như mình, đây là một bức tường thuật ngữ khó chịu."
    },
    {
        "uc": "Use Case 2",
        "title": "Proposed HCI Solutions",
        "content": """
            <ul>
                <li><strong>Inline Progressive Disclosure Scaffolding</strong>
                    <br>Add an info icon (ⓘ) next to ambiguous metrics revealing a one-line overlay definition (e.g., <em>"Moving Time: Time actively in motion"</em>).</li>
                <li><strong>HCI Principle:</strong> Shifts interface from high-effort <em>recall</em> to effortless <em>recognition</em>.</li>
            </ul>
        """,
        "image": "",
        "notes": "Giải pháp chỉ tốn của dev đúng 10 phút: Gắn một cái icon Info (chữ i) bé xíu. Bấm vào nó giải thích 'Moving time là thời gian bạn thực sự di chuyển'. Kỹ thuật Progressive Disclosure (tiết lộ dần) này sẽ cứu vớt toàn bộ trải nghiệm đọc hiểu."
    },
    # UC3
    {
        "uc": "Use Case 3",
        "title": "Overview: Exploring Maps & Segments",
        "content": """
            <ul>
                <li><strong>Goal:</strong> Discover routes and competitive sections ("Segments").</li>
                <li><strong>Interface:</strong> Maps Tab → Routes List → Popular Segments Map Overlay.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0529.PNG",
        "image_class": "phone",
        "notes": "Luồng số 3: Xem bản đồ. Mình tò mò muốn biết tính năng nổi bật nhất của Strava là 'Segments' (đoạn đường) trông như thế nào."
    },
    {
        "uc": "Use Case 3",
        "title": "User Interaction Context",
        "content": """
            <ul>
                <li><strong>Environmental State:</strong> Relaxed indoor, trip planning.</li>
                <li><strong>Interaction Method:</strong> Multi-axis panning, pinch-to-zoom, horizontal tab toggling.</li>
                <li><strong>Implicit Expectation:</strong> Quickly understand map markers and filters without external explanation.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0530.PNG",
        "image_class": "phone",
        "notes": "Lúc này mình đang rảnh rỗi ngồi quẹt bản đồ. Đập vào mắt là vô số các ghim (pins) trên bản đồ và hàng loạt các tab."
    },
    {
        "uc": "Use Case 3",
        "title": "Use Case Interactions",
        "content": """
            <ul>
                <li><strong>Step 1:</strong> Tap central "Maps" icon.</li>
                <li><strong>Step 2:</strong> Swipe across top pill-button filter row.</li>
                <li><strong>Step 3:</strong> Tap "Segments" tab to view section rankings.</li>
                <li><strong>Step 4:</strong> Pinch and drag to navigate map.</li>
            </ul>
        """,
        "image": "",
        "notes": "Mình đã phải quẹt qua lại, bấm thử vào nút 'Segments' rồi xem trên màn hình có gì thay đổi không để tự đoán xem tính năng này làm cái gì."
    },
    {
        "uc": "Use Case 3",
        "title": "Human Capabilities Matrix",
        "content": """
            <div class="grid-2x1">
                <div>
                    <h4>Vision & Touch</h4>
                    <p class="drawback">Drawback: Dense overlapping pins increase visual search time. Tiny map pin targets require high precision.</p>
                </div>
                <div>
                    <h4>Memory & Cognition</h4>
                    <p class="drawback highlight-text">Drawback: Proprietary terminology ("Segment") with zero onboarding strains working memory.</p>
                </div>
            </div>
        """,
        "image": "",
        "notes": "Điểm mấu chốt ở đây không nằm ở thị giác hay thao tác, mà nằm ở bộ nhớ làm việc (working memory). Chữ 'Segment' không hề có trong từ điển bản đồ thông thường. Strava bắt mình nạp một khái niệm hoàn toàn mới mà không thèm đưa ra một lời giải thích nào."
    },
    {
        "uc": "Use Case 3",
        "title": "User Mental Model Analysis",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>The Jargon Barrier:</strong> "Segment" lacks context; does not map to existing mental models.</li>
                <li class="drawback"><strong>Learning via Trial & Error:</strong> Recursively clicking tabs to decode features.</li>
            </ul>
            <blockquote>"No, I really didn't understand it... I had to try tapping several tabs before I understood."</blockquote>
        """,
        "image": "strava-images/IMG_0530.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Cú sốc về Mental Model: App bắt mình học cách sử dụng bằng phương pháp Trial-and-Error (Thử và Sai). Mình bấm đại để xem có gì xảy ra. Trong thiết kế UI/UX, khi bạn ép người dùng phải 'đoán' xem nút này làm gì thay vì 'đọc' xem nó làm gì, đó là một thiết kế thất bại về mặt giao tiếp."
    },
    {
        "uc": "Use Case 3",
        "title": "Interaction Metaphors",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>Affordance Mismatch:</strong> "Segments" shares identical visual styling with basic filters like "Length", "Elevation", "Surface".</li>
                <li><strong>HCI Impact:</strong> Identical styling incorrectly implies equal simplicity, misleading exploration.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0530.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Lỗi cực lớn về Affordance (đặc tính gợi ý thao tác): Strava thiết kế tab 'Segments' y hệt như các tab lọc như 'Độ dài', 'Độ dốc'. Khi hai thứ có vẻ ngoài giống nhau, não bộ tự động đánh giá mức độ dễ hiểu của chúng là ngang nhau. Nhưng thực tế 'Độ dốc' ai cũng hiểu, còn 'Segment' thì không. Sự đánh lừa thị giác này làm trải nghiệm trở nên bực bội."
    },
    {
        "uc": "Use Case 3",
        "title": "Usability Diagnostic",
        "content": """
            <ul>
                <li><strong>Learnability:</strong> Poor. First-time users cannot understand purpose from label alone.</li>
                <li><strong>Efficiency:</strong> Low. Trial-and-error wastes time.</li>
                <li><strong>Memorability:</strong> Moderate (once manually decoded).</li>
            </ul>
        """,
        "image": "",
        "notes": "Rõ ràng Learnability (tính dễ học) gần như bằng không. Người dùng phải tốn thời gian vô ích để tự học luật chơi của app."
    },
    {
        "uc": "Use Case 3",
        "title": "Proposed HCI Solutions",
        "content": """
            <ul>
                <li><strong>Contextual Dynamic Subtext Scaffolding</strong>
                    <br>Display a helpful one-line subtitle: <em>"Segments: Popular timed road sections where you compare times..."</em></li>
                <li><strong>HCI Principle:</strong> Replaces blind trial-and-error with clear <em>recognition</em>.</li>
            </ul>
        """,
        "image": "",
        "notes": "Giải quyết cực dễ: Khi lần đầu người dùng vào tab này, chèn thêm đúng 1 dòng text phụ bên dưới: 'Đoạn đường (Segments): Khu vực mọi người đua thời gian'. Xong! Một câu nói đơn giản biến sự mò mẫm thành một tính năng cực kỳ rõ ràng."
    },
    # UC4
    {
        "uc": "Use Case 4",
        "title": "Overview: Groups (Challenges & Clubs)",
        "content": """
            <ul>
                <li><strong>Goal:</strong> Find and join local clubs and fitness challenges.</li>
                <li><strong>The Paradox:</strong> Motivated users encounter major visual distractions and navigation blocks.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0532.PNG",
        "image_class": "phone",
        "notes": "Luồng 4: Tìm nhóm. Ở đây mình có mục tiêu rất cụ thể: Tìm một nhóm chạy quanh khu nhà mình."
    },
    {
        "uc": "Use Case 4",
        "title": "User Interaction Context",
        "content": """
            <ul>
                <li><strong>User Intent:</strong> Locate active running club in local area.</li>
                <li><strong>Observed Behavior:</strong> Eye bypasses card text and jumps straight to the bright "Join" button.</li>
            </ul>
            <blockquote>"When I see a card... I focus on the button and tap it without reading... I assume I need to enter another space to see details."</blockquote>
        """,
        "image": "strava-images/IMG_0533.PNG",
        "image_class": "phone",
        "notes": "Nhưng khi vừa vào giao diện, mắt mình bị khóa chặt vào nút Join màu cam rực rỡ. Mình bấm thẳng vào nó theo phản xạ mà thậm chí chưa kịp đọc xem câu lạc bộ đó tên là gì."
    },
    {
        "uc": "Use Case 4",
        "title": "Human Capabilities Matrix",
        "content": """
            <div class="grid-2x1">
                <div>
                    <h4>Vision & Attention</h4>
                    <p class="drawback highlight-text">Drawback: High-contrast "Join" button grabs peripheral vision (foveal pull), tricking users into premature taps.</p>
                </div>
                <div>
                    <h4>Memory & Cognition</h4>
                    <p class="drawback">Drawback: Single touch surface handles two different actions, overloading focus.</p>
                </div>
            </div>
        """,
        "image": "",
        "notes": "Strava đã dùng hiệu ứng thị giác (foveal pull) quá đà. Nút Join quá nổi bật, lôi kéo hoàn toàn sự chú ý ngoại vi. Nhưng cái tệ nhất là thiết kế này gộp hai thứ: 'Nhấn để tham gia' và 'Nhấn để xem chi tiết' vào cùng một cụm thẻ mà không phân chia rõ ràng."
    },
    {
        "uc": "Use Case 4",
        "title": "User Mental Model Analysis",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>The Expectation:</strong> Tapping primary CTA opens rich detail screen (standard card convention).</li>
                <li class="drawback"><strong>The Reality:</strong> In-place state toggle. No navigation.</li>
                <li><strong>HCI Violation:</strong> Fails Golden Rule #3 (Offer informative feedback) for exploring details.</li>
            </ul>
            <blockquote>"Nothing happens... What I expect is that it jumps into more detail... I got stuck."</blockquote>
        """,
        "image": "strava-images/IMG_0533.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Mental model của mình là: Nhấn vào nút bự trên một cái thẻ -> Thẻ mở to ra cho mình đọc. Thực tế: Mình bấm Join, nút nhấp nháy chuyển màu. Thẻ ĐỨNG IM. Mình bị kẹt lại vì không biết làm sao để mở đọc chi tiết cả. Strava cung cấp feedback cho việc Join, nhưng lại hoàn toàn câm điếc (zero visibility) trong việc làm sao để xem thông tin."
    },
    {
        "uc": "Use Case 4",
        "title": "Interaction Metaphors",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>Affordance Blurring:</strong> Blends State Toggling (joining) and Navigation (viewing details) into single visual block.</li>
                <li><strong>HCI Failure:</strong> Violates consistency and affordance. Different actions must look distinct.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0533.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Sự pha trộn Affordance này là một lỗi ngớ ngẩn. Việc nhấn công tắc (toggle state) và Việc lật sang trang (navigation) là 2 hành động hoàn toàn khác nhau. Ép chúng lên cùng một mặt phẳng thị giác giống như việc bạn vẽ nút Xóa sát cạnh nút Lưu vậy."
    },
    {
        "uc": "Use Case 4",
        "title": "Task Analysis Gap",
        "content": """
            <ul>
                <li class="drawback highlight-text"><strong>Stated Goal:</strong> "Find an active running club near my location."</li>
                <li class="drawback"><strong>Interface Failure:</strong> Shows marketing promo ("Create Your Own") and official Strava Club only.</li>
                <li><strong>HCI Evaluation:</strong> Zero achievement rate for a primary user goal due to missing local search filters.</li>
            </ul>
        """,
        "image": "strava-images/IMG_0534.PNG",
        "image_class": "phone highlight-problem",
        "notes": "Trầm trọng hơn, nhu cầu thực sự của mình là 'Tìm nhóm quanh đây' thì KHÔNG THỂ THỰC HIỆN ĐƯỢC. Màn hình chỉ hiện dòng chữ 'Hãy tự tạo club của bạn đi' và 1 nhóm của Strava. Không có công cụ tìm kiếm vị trí. Strava phân tích user task (task analysis) ở mục này hoàn toàn trượt mục tiêu thực tế."
    },
    {
        "uc": "Use Case 4",
        "title": "Proposed HCI Solutions",
        "content": """
            <ul>
                <li><strong>A: Structural Affordance Separation</strong>
                    <br>Card body opens details (signaled by arrow); shrink "Join" into separate button container.</li>
                <li><strong>B: Direct Navigation Feedback</strong>
                    <br>After joining: <em>"Joined! Tap here to view details."</em></li>
                <li><strong>C: Goal-Driven Search Integration</strong>
                    <br>Add prominent "Find a Club Near You" search bar with geolocation.</li>
            </ul>
        """,
        "image": "",
        "notes": "Giải pháp: Thứ nhất, tách bạch rõ ràng! Làm nhỏ cái nút Join lại để chừa chỗ cho một nút 'Xem chi tiết'. Hoặc ít nhất bấm Join xong thì báo 'Đã tham gia, ấn vô đây để xem chi tiết'. Thứ ba, làm ơn thêm thanh tìm kiếm theo GPS để giải quyết đúng cái Task (nhiệm vụ) mà người dùng cần."
    },
    # Closing
    {
        "uc": "CONCLUSION",
        "title": "Key Strategic Takeaways",
        "content": """
            <ul>
                <li><strong>Core Recording Loop:</strong> Highly intuitive and easy to use <span style="color:green;">✓</span></li>
                <li><strong>Supporting Workflows:</strong> Suffer from confusing jargon, hidden navigation, abrupt popups <span style="color:red;">✕</span></li>
                <li><strong>The Path Forward:</strong> Clear task closure points, helpful inline definitions, distinct buttons for distinct actions.</li>
            </ul>
        """,
        "image": "",
        "notes": "Tổng kết lại: Tính năng cốt lõi (Ghi lại đường chạy) rất tốt. Nhưng các tính năng xoay quanh nó thì dở tệ vì Strava mắc kẹt giữa việc ép người dùng tương tác xã hội (social) và dùng quá nhiều từ lóng. Bài học rút ra là: Hãy cho người dùng cảm giác hoàn thành rõ ràng (closure), giải thích các từ ngữ chuyên ngành bằng ngôn ngữ bình dân, và tách biệt rõ ràng các hành động giao diện."
    },
    {
        "uc": "CONCLUSION",
        "title": "Final Q&A Session",
        "content": """
            <ul>
                <li>Thank You for Your Attention</li>
                <li>Questions & Discussion</li>
                <li>UI/UX Product Research Report — Strava Platform</li>
                <li>CSC13112 · Group 03 · FIT-HCMUS</li>
            </ul>
        """,
        "image": "",
        "notes": "Cảm ơn thầy và các bạn đã lắng nghe. Mời mọi người đặt câu hỏi!"
    }
]

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strava - Product Research & Interaction Analysis</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/white.min.css">
    <style>
        .reveal .slides {
            text-align: left;
        }
        .reveal section {
            height: 100%;
            padding-top: 60px !important;
        }
        .reveal h2 {
            font-size: 1.6em;
            color: navy;
            text-transform: none;
            margin-bottom: 30px;
        }
        .reveal p, .reveal li {
            font-size: 0.65em;
            line-height: 1.4;
        }
        .reveal li {
            margin-bottom: 12px;
        }
        .header-badge {
            position: absolute;
            top: -20px;
            left: 0;
            background: #ff7f50;
            color: white;
            padding: 8px 15px;
            border-radius: 6px;
            font-size: 0.5em;
            font-weight: bold;
            z-index: 10;
        }
        .header-title {
            position: absolute;
            top: -15px;
            right: 0;
            color: navy;
            font-size: 0.5em;
            font-weight: bold;
            z-index: 10;
        }
        .slide-content-wrapper {
            display: flex;
            gap: 40px;
            align-items: flex-start;
            margin-top: 20px;
        }
        .text-column {
            flex: 1;
        }
        .image-column {
            flex: 0 0 300px;
            display: flex;
            justify-content: center;
        }
        .reveal img.phone {
            border-radius: 20px;
            border: 2px solid #e0e0e0;
            aspect-ratio: 9/16;
            object-fit: cover;
            max-height: 520px;
            margin: 0;
        }
        .reveal img.background-blur {
            opacity: 0.2;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
            border: none;
            border-radius: 0;
        }
        .highlight-problem {
            border: 4px solid #ff7f50 !important;
            box-shadow: 0 0 20px rgba(255,127,80,0.6);
        }
        .highlight-solution {
            border: 4px solid #4caf50 !important;
            box-shadow: 0 0 20px rgba(76,175,80,0.6);
        }
        .highlight-text {
            background-color: rgba(255,127,80,0.1);
            padding: 5px;
            border-left: 4px solid #ff7f50;
        }
        .benefit {
            border-left: 4px solid #4caf50;
            padding-left: 10px;
        }
        .drawback {
            border-left: 4px solid #ff7f50;
            padding-left: 10px;
        }
        .grid-2x2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .grid-2x1 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .card {
            background: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #eee;
        }
        .card h4 {
            font-size: 1.1em;
            margin-top: 0;
            color: #333;
            margin-bottom: 10px;
        }
        .card p {
            margin-bottom: 8px;
            font-size: 0.9em;
        }
        blockquote {
            font-style: italic;
            border-left: 4px solid #ccc;
            padding-left: 15px;
            color: #666;
            background: #f4f4f4;
            padding: 10px 15px;
            border-radius: 0 8px 8px 0;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
'''

for slide in slides:
    html_template += "            <section>\n"
    if slide['uc']:
        html_template += f"                <div class=\"header-badge\">{slide['uc']}</div>\n"
    html_template += "                <div class=\"header-title\">STRAVA</div>\n"
    
    # Check if this slide has a background image
    if slide.get('image') and 'background-blur' in slide.get('image_class', ''):
        html_template += f"                <img src=\"{slide['image']}\" class=\"{slide['image_class']}\" alt=\"Background\">\n"
        
    html_template += f"                <h2>{slide['title']}</h2>\n"
    
    html_template += "                <div class=\"slide-content-wrapper\">\n"
    html_template += "                    <div class=\"text-column\">\n"
    html_template += f"                        {slide['content']}\n"
    html_template += "                    </div>\n"
    
    # Check if this slide has a side image
    if slide.get('image') and 'background-blur' not in slide.get('image_class', ''):
        html_template += "                    <div class=\"image-column\">\n"
        html_template += f"                        <img src=\"{slide['image']}\" class=\"{slide['image_class']}\" alt=\"Slide image\">\n"
        html_template += "                    </div>\n"
        
    html_template += "                </div>\n"
    
    html_template += "                <aside class=\"notes\">\n"
    html_template += f"                    {slide['notes']}\n"
    html_template += "                </aside>\n"
    html_template += "            </section>\n"

html_template += '''
        </div>
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/notes/notes.min.js"></script>
    <script>
        Reveal.initialize({
            plugins: [ RevealNotes ],
            slideNumber: true,
            hash: true,
            center: false,
            transition: 'slide',
            backgroundTransition: 'fade'
        });
    </script>
</body>
</html>
'''

with open("final_slides.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Slides generated successfully in final_slides.html")
