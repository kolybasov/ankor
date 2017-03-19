// used to close notifications, modals, etc
const deleteParentBox = (evt) => {
  const notificationsBox = event.target.closest('section.notifications');
  notificationsBox.parentNode.removeChild(notificationsBox);
};
