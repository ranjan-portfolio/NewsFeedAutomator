from tools.deploy_s3 import deploy_html_toS3

html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Newz Bytezz</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .navbar {
            background-color: #333;
            overflow: hidden;
        }
        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        .container {
            padding: 20px;
        }
        .article {
            margin-bottom: 40px;
        }
        .article-title {
            font-weight: bold;
            font-size: 1.5em;
            margin-bottom: 10px;
        }
        .article-content {
            font-size: 1em;
            line-height: 1.6;
        }
    </style>
</head>
<body>

<div class="navbar">
    <a href="#duolingo-ai">Duolingo CEO Clarifies AI Ambitions Amidst Misunderstandings</a>
    <!-- Add more navbar links here -->
    <a href="#flip-phone">Dust Resistance: The Achilles' Heel of the Flip Phone Era</a>
    <a href="#minimalism-tech">Minimalism Meets Tech Chaos: A Peek into Popular Trends</a>
    <a href="#airpods-pro">Snag the AirPods Pro 2 for Just $169</a>
    <a href="#meta-ai">Meta Under Fire as Senator Investigates AI Chats with Minors</a>
    <a href="#retro-shooting">Retro Shooting Fun with Camp Snap CS-8</a>
    <a href="#electric-constant">Unveiling the Universe's Glue: The Electric Constant Explained</a>
    <a href="#mattress-topper">Mattress Topper Match-Up: Top Picks and Those That Just Missed</a>
    <a href="#pixel-cases">Pixel 9 Cases: Editor's Picks and Meh Mentions</a>
    <a href="#ai-physics">AI Breaks New Ground in Physics Experimentation</a>
</div>

<div class="container">
    <div class="article" id="duolingo-ai">
        <div class="article-title">Duolingo CEO Clarifies AI Ambitions Amidst Misunderstandings</div>
        <div class="article-content">
            Duolingo CEO Luis von Ahn addressed public criticisms of his plan to make Duolingo an "AI-first company," stating that the backlash stemmed from a lack of context in his initial announcement. He emphasized that the strategy does not involve laying off full-time employees and remains confident in AI's potential, with staff dedicating time weekly to explore AI technologies.
        </div>
    </div>

    <!-- Add more articles here in a similar fashion -->

    <div class="article" id="flip-phone">
        <div class="article-title">Dust Resistance: The Achilles' Heel of the Flip Phone Era</div>
        <div class="article-content">
            The appeal of flip phones lies in their unique design and user engagement, but despite innovations from brands like Motorola and Samsung, these devices struggle with a significant drawback—dust resistance. While other high-end phones boast an IP68 rating, flip phones offer limited dust protection, making them a tough sell at their premium price points; the persistent issue of dust infiltration, despite advancements in screen and hinge durability, prevents full-throated recommendations for these otherwise compelling devices.
        </div>
    </div>

    <div class="article" id="minimalism-tech">
        <div class="article-title">Minimalism Meets Tech Chaos: A Peek into Popular Trends</div>
        <div class="article-content">
            The latest edition of Installer highlights intriguing tech-driven content, including a dive into minimalistic smartphone home screens and current cultural obsessions, such as retro games and unique creations like giant anthropomorphic Furbys. Alongside community recommendations and upcoming product launch excitement, tech enthusiast Soren Iverson inspires a stripped-down digital life approach focused on intentionality and simplicity.
        </div>
    </div>

    <div class="article" id="airpods-pro">
        <div class="article-title">Snag the AirPods Pro 2 for Just $169</div>
        <div class="article-content">
            The AirPods Pro 2 are available for an impressive discount of $80, bringing their price down to $169 at Amazon as of August 17. Known for their rich sound and best-in-class noise cancellation, these earbuds are a top choice for portability and seamless integration within the Apple ecosystem.
        </div>
    </div>

    <div class="article" id="meta-ai">
        <div class="article-title">Meta Under Fire as Senator Investigates AI Chats with Minors</div>
        <div class="article-content">
            Missouri Senator Josh Hawley has launched an investigation into Meta after reports that its AI chatbots were allowed to engage in "sensual" conversations with children. Hawley, who chairs the Senate Judiciary Committee Subcommittee on Crime and Counterterrorism, demands transparency from the tech giant regarding its AI policies and warns against potential exploitation and deception risks posed to minors.
        </div>
    </div>

    <div class="article" id="retro-shooting">
        <div class="article-title">Retro Shooting Fun with Camp Snap CS-8</div>
        <div class="article-content">
            The Camp Snap CS-8 embraces simplicity and nostalgia, offering a straightforward, playful experience reminiscent of Super 8 camcorders from the 1960s. Designed with a retro aesthetic and equipped with basic controls, it encourages a focus on the joy of filming without the frills, boasting digital effects that lend a charming, imperfect quality to your videos.
        </div>
    </div>

    <div class="article" id="electric-constant">
        <div class="article-title">Unveiling the Universe's Glue: The Electric Constant Explained</div>
        <div class="article-content">
            The electric constant, a fundamental value crucial to calculating forces between electric charges, plays a vital role in the formation of matter as we know it. By allowing us to understand how electrons interact to form molecules, this constant is essential to the universe's capability to support life, though its origins and interrelations with other physical constants remain a profound mystery worth exploring.
        </div>
    </div>

    <div class="article" id="mattress-topper">
        <div class="article-title">Mattress Topper Match-Up: Top Picks and Those That Just Missed</div>
        <div class="article-content">
            In a comprehensive review of mattress toppers, the Avocado Alpaca Topper and Helix Dual Comfort Mattress Topper were highlighted as luxurious options for those seeking comfort tailored to different firmness preferences. While a variety of options like the Brooklyn Bedding Latex and Tempur-Pedic toppers offered distinct benefits, ranging from natural materials to innovative memory foam, some offerings like the Leesa Mattress Topper did not meet the testing standards due to quality issues. This roundup provides insight into quality bedding solutions tailored to various sleeping preferences and budgets.
        </div>
    </div>

    <div class="article" id="pixel-cases">
        <div class="article-title">Pixel 9 Cases: Editor's Picks and Meh Mentions</div>
        <div class="article-content">
            The article reviews an extensive range of Pixel 9 accessories, highlighting the Spigen Tough Armor and OtterBox Defender as top choices for protection and feature utility. It also mentions other notable cases and accessories like the UAG Tempered Glass Screen Protector and the Pela Liquid Screen Protector, offering varied levels of appeal, functionality, and design, while advising against some less impressive options like the OtterBox Thin Flex Series.
        </div>
    </div>

    <div class="article" id="ai-physics">
        <div class="article-title">AI Breaks New Ground in Physics Experimentation</div>
        <div class="article-content">
            Artificial intelligence is making significant strides in the world of physics, designing innovative and effective experiments previously unimagined by human researchers. Though AI hasn't revealed new discoveries yet, its ability to identify complex patterns—such as Einstein's symmetries at the Large Hadron Collider—and to contribute to quantum entanglement research highlights its growing role as a catalyst for breakthrough developments in the field.
        </div>
    </div>
</div>

</body>
</html>

'''

response=deploy_html_toS3(html)

print(response)