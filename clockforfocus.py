import pygame
import time

# 初始化 Pygame
pygame.init()

# 定义窗口大小
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# 创建窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Focus Timer')

# 定义字体
font = pygame.font.SysFont('Arial', 60)

# 定义倒计时函数
def countdown(t):
    while t > 0:
        # 将剩余时间转换为分钟和秒
        mins, secs = divmod(t, 60)
        # 格式化时间字符串
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 清空窗口
        window.fill((255, 255, 255))
        # 创建文本对象
        text = font.render(timer, True, (0, 0, 0))
        # 将文本对象绘制到窗口中心
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text, text_rect)
        # 更新窗口
        pygame.display.update()
        # 等待一秒钟
        time.sleep(1)
        # 减少剩余时间
        t -= 1

    # 倒计时结束，显示消息
    window.fill((255, 255, 255))
    text = font.render('Time is up!', True, (0, 0, 0))
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text, text_rect)
    pygame.display.update()

# 定义专注时长（以秒为单位）
focus_duration = 25 * 60

# 启动倒计时
countdown(focus_duration)

# 等待用户关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
